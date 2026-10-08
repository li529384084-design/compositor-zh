# -*- coding: utf-8 -*-
"""Compositor 界面汉化对照表：英文原文 → 简体中文。

替换方式为「整条字符串字面量精确匹配」，所以原文必须与 Swift 源码里
双引号之间的内容逐字符一致（含省略号、破折号、弯引号）。
插值片段（\\(...)）保持原样不动。

分四组：
  MENU        菜单栏与命令
  PANEL       工具选项面板（侧栏）
  SHEET       各类对话框 / 表单
  EXTRA       枚举显示名、AppKit 菜单项、图层默认命名等
"""

ZH = {}

# ---------------------------------------------------------------- 菜单栏 / 命令
ZH.update({
    # 编辑
    "Undo": "撤销",
    "Redo": "重做",
    "Cut": "剪切",
    "Copy": "拷贝",
    "Copy Merged": "合并拷贝",
    "Paste": "粘贴",
    "Fill with Foreground Color": "填充前景色",
    "Fill with Background Color": "填充背景色",
    "Clear Selection Pixels": "清除选区像素",
    "Content-Aware Fill…": "内容识别填充…",
    "Keyboard Shortcuts…": "键盘快捷键…",
    "Command Palette…": "命令面板…",

    # 文件
    "New Canvas…": "新建画布…",
    "Open Project…": "打开项目…",
    "Open Recent": "打开最近使用",
    "Clear Menu": "清除菜单",
    "Import Images…": "导入图像…",
    "Save": "存储",
    "Save As…": "存储为…",
    "Export PNG…": "导出 PNG…",
    "Export JPEG…": "导出 JPEG…",
    "Close Project": "关闭项目",
    "Check for Updates…": "检查更新…",

    # 显示
    "Canvas Only (F)": "仅显示画布 (F)",
    "Fit Canvas": "适合窗口",
    "Actual Pixels": "实际像素",
    "Zoom In": "放大",
    "Zoom Out": "缩小",
    "Pixel Grid (800% and above)": "像素网格（800% 及以上）",
    "Show Transform Controls": "显示变换控件",
    "Show": "显示",
    "Grid": "网格",
    "Guides": "参考线",
    "Grid Settings…": "网格设置…",
    "Rulers": "标尺",
    "Snap": "对齐",
    "Snap To": "对齐到",
    "Layers": "图层",
    "Document Bounds": "文档边界",
    "Lock Guides": "锁定参考线",
    "Clear Guides": "清除参考线",
    "Hide Compositor": "隐藏 Compositor",
    "Hide Others": "隐藏其他",
    "Show All": "显示全部",

    # 选择
    "Select": "选择",
    "All": "全部",
    "Deselect": "取消选择",
    "Inverse": "反选",
    "Layer's Pixels": "图层像素",
    "Subject": "主体",
    "Color Range…": "色彩范围…",
    "Mask's Black Areas": "蒙版黑色区域",
    "Expand…": "扩展…",
    "Contract…": "收缩…",
    "Feather…": "羽化…",

    # 图像
    "Image": "图像",
    "Curves…": "曲线…",
    "Levels…": "色阶…",
    "Hue/Saturation…": "色相/饱和度…",
    "Canvas Size…": "画布大小…",
    "Image Size…": "图像大小…",
    "Trim…": "裁切…",
    "Rotate Canvas 90° Clockwise": "顺时针旋转画布 90°",
    "Rotate Canvas 90° Counterclockwise": "逆时针旋转画布 90°",
    "Flip Canvas Horizontal": "水平翻转画布",
    "Flip Canvas Vertical": "垂直翻转画布",

    # 滤镜 / 图层
    "Filter": "滤镜",
    "Layer": "图层",
    "New Adjustment Layer": "新建调整图层",
    "Edit Adjustment…": "编辑调整…",
    "Group Selected Layers": "编组所选图层",
    "Ungroup Layers": "取消图层编组",
    "Move Out of Folder": "移出文件夹",
    "New Blank Layer": "新建空白图层",
    "Rename Layer…": "重命名图层…",
    "Move Layer Up": "上移图层",
    "Move Layer Down": "下移图层",
    "Flip Layer Horizontal": "水平翻转图层",
    "Flip Layer Vertical": "垂直翻转图层",
})

# ---------------------------------------------------------------- ContentView / 状态栏
ZH.update({
    "Eyedropper": "吸管",
    "Sample Ring": "取样环",
    "Select a tool": "选择工具",
    "New canvas": "新建画布",
    "New canvas (⌘N)": "新建画布 (⌘N)",
    "Fit": "适合窗口",
    "Fit canvas in window (⌘0)": "使画布适合窗口 (⌘0)",
    "Actual pixels (⌘1)": "实际像素 (⌘1)",
    "Zoom in (⌘+)": "放大 (⌘+)",
    "Zoom out (⌘−)": "缩小 (⌘−)",
    "Import couldn’t finish": "导入未能完成",
    "Couldn’t paint": "无法绘制",
    "Couldn’t crop": "无法裁剪",
    "sRGB · Transparent": "sRGB · 透明",
    "Ready when you are": "准备就绪",
    "Working…": "处理中…",
    "Importing images…": "正在导入图像…",
    "Drag to resize the panel": "拖动可调整面板宽度",
    "OK": "确定",
    "Cancel": "取消",
    "Apply": "应用",
    "Save": "存储",
    "Done": "完成",
    "Reset": "复位",
    "Apply Crop": "应用裁剪",
    "Resize": "调整大小",
    "Export…": "导出…",
    "Import": "导入",
    "Open project": "打开项目",
    "Import image": "导入图像",
    "Create canvas": "创建画布",
    "Create": "创建",
    "Remove": "移除",
    "Delete": "删除",
    "Close": "关闭",
    "Restore Defaults": "恢复默认值",
})

# ---------------------------------------------------------------- 工具选项面板
ZH.update({
    # 画笔
    "Mode": "模式",
    "Paint with the foreground color (B), or erase pixels away (E)":
        "用前景色绘画 (B)，或擦除像素 (E)",
    "Liquify pushes pixels · Blur softens · Smudge drags color along":
        "液化推移像素 · 模糊柔化边缘 · 涂抹拖带颜色",
    "Type": "类型",
    "Aligned": "对齐",
    "Keep the source moving with the brush between strokes; off starts every stroke at the source point":
        "笔画之间取样点跟随画笔移动；关闭后每一笔都从原取样点开始",
    "Sample": "取样",
    "This Layer": "当前图层",
    "All Layers": "所有图层",
    "Copy from the active layer only, or from every visible layer as shown":
        "只从当前图层复制，或从所有可见图层按显示效果复制",
    "Size": "大小",
    "Hardness": "硬度",
    "Opacity": "不透明度",
    "Press 1–9 for 10–90%, 0 for 100%": "按 1–9 设为 10–90%，按 0 设为 100%",
    "Radius": "半径",
    "How far the blur softens, in pixels": "模糊柔化的范围（像素）",
    "Smoothing": "平滑",
    "The brush trails the pointer on a string this long, so a shaky hand still draws a smooth line":
        "画笔像被这根长度的线牵引着跟随指针，手抖也能画出平滑的线",
    "Paint": "绘画",
    "Black · Hide": "黑色 · 隐藏",
    "White · Reveal": "白色 · 显示",
    "Color": "颜色",
    "Foreground color": "前景色",
    "Option-click to set the source": "按住 Option 单击可设置取样点",
    "Mask": "蒙版",

    # 选区（选框 / 套索 / 魔棒）
    "Shape": "形状",
    "Press M to switch between Rectangle and Ellipse": "按 M 在矩形与椭圆之间切换",
    "Press Tab to switch between Wand and Object": "按 Tab 在魔棒与对象之间切换",
    "Lasso": "套索",
    "Press L to switch between Freehand and Polygonal": "按 L 在手绘与多边形之间切换",
    "Hold Shift to add or Option to subtract for one outline": "按住 Shift 加选、按住 Option 减选（单次轮廓）",
    "Anti-alias": "消除锯齿",
    "Feather": "羽化",
    "Fade the edge of the selection by this many pixels": "按此像素数羽化选区边缘",
    "Empty selection": "空选区",
    "Tolerance": "容差",
    "How far each color channel (0–255) can differ from the clicked color and still be selected":
        "各颜色通道 (0–255) 与点击处颜色的差异在此范围内仍会被选中",
    "Sample Size": "取样大小",
    "Match the clicked pixel, or the average of the pixels around it":
        "匹配点击处单个像素，或取其周围像素的平均值",
    "Read colors from the active layer only, or from every visible layer as shown":
        "只读取当前图层的颜色，或读取所有可见图层按显示效果的颜色",
    "Contiguous": "连续",
    "Select only similar pixels connected to the one you click; off selects them everywhere":
        "只选中与点击处相连的相似像素；关闭后选中全图所有相似像素",
    "Analyze the active layer only, or every visible layer as shown":
        "只分析当前图层，或分析所有可见图层按显示效果",
    "Edge": "边缘",
    "Positive values tighten the detected mask inward; negative values expand it outward":
        "正值向内收紧检测到的蒙版，负值向外扩张",
    "Amount": "数量",
    "Enter a whole number from 1 to \\(maximum) px.": "请输入 1 到 \\(maximum) px 之间的整数。",

    # 形状
    "Shift-U (or Tab) steps through Rectangle, Ellipse and Line":
        "按 Shift-U（或 Tab）依次切换矩形、椭圆与直线",
    "Width": "宽度",
    "Round the rectangle's corners by this many pixels; 0 keeps them square":
        "按此像素数圆角化矩形四角；0 保持直角",
    "Fill": "填充",
    "Shapes fill with the foreground color; click to change it": "形状以前景色填充；单击可更改颜色",

    # 文字
    "Font face, including bold and italic variants": "字体，含粗体与斜体变体",
    "Text color": "文字颜色",
    "Align ": "对齐 ",
    "Tracking": "字距",
    "Leading": "行距",
    "Auto": "自动",
    "Line height, baseline to baseline. Empty or 0 is Auto: 120% of the font size.":
        "行高（基线到基线）。留空或填 0 为自动：字号的 120%。",
    "Edit Text": "编辑文字",

    # 渐变
    "Gradient": "渐变",
    "Linear runs along the line; Radial spreads out from the start point":
        "线性沿直线方向延伸；径向从起点向外扩散",
    "Colors": "颜色",
    "Reverse": "反向",

    # 变换
    "Auto Select": "自动选择",
    "Select layers by clicking the canvas. Hold Command to turn it the other way while you click.":
        "在画布上单击即可选择图层。单击时按住 Command 可临时反向。",
    "Show Controls": "显示控件",
    "Show the transform box and handles (⌘H). When hidden, drag anywhere to move the layer.":
        "显示变换框与控制点 (⌘H)。隐藏时可在任意位置拖动移动图层。",
    "Lock aspect ratio. Hold Shift while dragging a handle to turn it the other way.":
        "锁定长宽比。拖动控制点时按住 Shift 可临时反向。",
    "Scale width and height together, about the center": "以中心为基准同比缩放宽度与高度",
    "Sampling": "取样",
    "Flip H": "水平翻转",
    "Flip V": "垂直翻转",

    # 图层外观 / 图层面板
    "Blend": "混合",
    "Opacity percent": "不透明度百分比",
    "%": "%",
    "No layers yet": "暂无图层",
    "New blank layer (⇧⌘N)": "新建空白图层 (⇧⌘N)",
    "New blank layer": "新建空白图层",
    "Group selected layers (⌘G)": "编组所选图层 (⌘G)",
    "New folder": "新建文件夹",
    "Add layer effect": "添加图层效果",
    "Layer effects": "图层效果",
    "New adjustment layer": "新建调整图层",
    "Add layer mask": "添加图层蒙版",

    # 调色板 / 缩放
    "Swap foreground and background (X)": "切换前景色与背景色 (X)",
    "Swap colors": "切换颜色",
    "Default colors (D)": "默认颜色 (D)",
    "Default colors": "默认颜色",
    "Zoom": "缩放",
    "Zoom percentage": "缩放百分比",
    "Zoom percentage (0.1–3200%). Press Return to apply.": "缩放百分比 (0.1–3200%)。按 Return 应用。",

    # 裁剪 / 曲线
    "Crop": "裁剪",
    "Ratio": "比例",
    "Click to add a point. Drag to adjust.": "单击添加控制点，拖动可调整。",
    "Input \\(Int(points[selected].x)) · Output \\(Int(points[selected].y))":
        "输入 \\(Int(points[selected].x)) · 输出 \\(Int(points[selected].y))",
    "Remove point": "移除控制点",
    "Reset curve": "复位曲线",
})

# ---------------------------------------------------------------- 对话框 / 表单
ZH.update({
    # 画布大小
    "Canvas Size": "画布大小",
    "Units": "单位",
    "Height": "高度",
    "Relative to current dimensions": "相对于当前尺寸",
    "Lock original aspect ratio": "锁定原始长宽比",
    "Anchor": "定位",
    "Keeps this point fixed. Artwork is not scaled; cropped content remains outside the canvas.":
        "保持此点不动。图像不会缩放；被裁掉的内容仍保留在画布之外。",
    "Canvas extension": "画布扩展",
    "Extension color": "扩展颜色",
    "Color for the added canvas": "新增画布区域的颜色",

    # 图像大小
    "Image Size": "图像大小",
    "Lock aspect ratio": "锁定长宽比",
    "Resolution": "分辨率",
    "pixels/inch": "像素/英寸",
    "Resample": "重新取样",
    "Resizes layer pixels and applies existing transforms. Undo restores the originals.":
        "重设图层像素并应用现有变换。撤销可恢复原状。",
    "Only print dimensions and resolution change. Pixels stay unchanged.":
        "仅打印尺寸与分辨率变化，像素保持不变。",

    # 网格设置
    "Gridline every": "网格线间隔",
    "pixels": "像素",
    "Subdivisions": "子网格",
    "Choose a custom grid color": "选择自定义网格颜色",

    # 裁切
    "Based On": "基于",
    "Trim Away": "裁切掉",
    "Top": "顶部",
    "Bottom": "底部",
    "Left": "左侧",
    "Right": "右侧",

    # 色相/饱和度
    "Range": "范围",
    "Apply outside this range instead": "改为调整此范围之外的区域",
    "Colorize": "着色",
    "Preview": "预览",
    "Limited to the selection": "仅限选区",
    "Targeted adjustment: drag on the image to change that color's saturation, or its hue with Command held":
        "目标调整：在图像上拖动可改变该颜色的饱和度，按住 Command 则改变色相",
    "Targeted adjustment": "目标调整",
    "Click the original layer to set \\(mode.rawValue.lowercased()). Click the eyedropper again to stop.":
        "在原始图层上单击以设置\\(mode.rawValue.lowercased())。再次单击吸管可退出。",

    # 色阶
    "Loading histogram…": "正在载入直方图…",
    "Linear histogram with automatic vertical scaling. Tall spikes may extend beyond the graph; all tones from 0 to 255 remain included.":
        "纵向自动缩放的线性直方图。过高的尖峰可能超出图框，0 到 255 的所有色调仍在统计范围内。",

    # 色彩范围
    "Fuzziness": "颜色容差",
    "How far a color may be from the picked ones and still be selected":
        "颜色与取样色的差异在此范围内仍会被选中",
    "Invert": "反相",
    "Select everything except those colors, such as all but a green screen":
        "选中除这些颜色以外的全部内容，例如抠掉绿幕区域",

    # 效果
    "Stroke": "描边",
    "Position": "位置",
    "Outside": "外部",
    "Inside": "内部",
    "Drop Shadow": "投影",
    "Color Overlay": "颜色叠加",
    "Inner Shadow": "内阴影",
    "Outer Glow": "外发光",
    "Inner Glow": "内发光",

    # JPEG 导出
    "Export JPEG": "导出 JPEG",
    "Show the whole image (⌘0)": "显示整幅图像 (⌘0)",
    "Zoom in (⌘+), now \\(percent). At 100% each pixel of the JPEG is one pixel of the screen, as on the canvas":
        "放大 (⌘+)，当前 \\(percent)。100% 时 JPEG 的每个像素对应屏幕的一个像素，与画布一致",
    "Zoom out (⌘−), now \\(percent)": "缩小 (⌘−)，当前 \\(percent)",
    "Drag or scroll to move around; double-click switches between Fit and 100%":
        "拖动或滚动可平移视图；双击可在适合窗口与 100% 之间切换",
    "Quality": "品质",
    "Background for transparency": "透明区域背景",
    "Color that fills transparent areas": "用于填充透明区域的颜色",
    "Updating…": "正在更新…",

    # 新建画布
    "Size": "大小",
    "Custom": "自定",
    "Preset sizes for screens and common formats": "屏幕与常见格式的预设尺寸",
    "Preset sizes": "预设尺寸",

    # 项目标签
    "Project tabs": "项目标签",
    "New": "新建",
    "Drop to open in a new canvas": "拖放到此处可在新画布中打开",
    "Drop into new canvas": "拖入新画布",
    "Unsaved changes": "有未存储的更改",
    "Close \\(tab.title)": "关闭 \\(tab.title)",

    # 其他
    "Reading the Photoshop file…": "正在读取 Photoshop 文件…",
    "Develop “\\(url.lastPathComponent)”": "调整“\\(url.lastPathComponent)”",
    "Importing…": "正在导入…",
    "Search commands and tools": "搜索命令与工具",
    "No commands match": "没有匹配的命令",
    "Search shortcuts": "搜索快捷键",
    "Click a shortcut, then press its new key combination. Changes apply when you save.":
        "单击一个快捷键，然后按下新的组合键。存储后生效。",
    "Contextual keys & mouse gestures": "上下文按键与鼠标手势",
    "Text fields keep standard macOS editing keys. Dialogs share the Apply/Cancel assignments above. Numeric fields use Up/Down, with Shift for larger steps. Standard macOS commands include ⌘Q to quit and ⌃⌘F for full screen. The shortcut editor itself always uses Return to save and Esc to cancel when not recording.":
        "文本输入框保留 macOS 标准编辑按键。对话框共用上方「应用/取消」的分配。数值输入框使用上/下方向键，按住 Shift 可加大步长。macOS 标准命令包括 ⌘Q 退出与 ⌃⌘F 全屏。快捷键编辑器本身在未录制时始终使用 Return 存储、Esc 取消。",
    "Option temporarily selects the eyedropper in painting tools. Shift constrains shapes/movement or adds to a selection; Option subtracts from selections or draws from center. Command-drag moves selected pixels; Command-Option-drag copies them. Option-drag duplicates layers/folders/effects; Option-click at a layer boundary toggles clipping. Command-click a thumbnail loads its selection. Control bypasses snapping. Right-drag adjusts brush size. Modifier-and-mouse gestures are fixed.":
        "在绘画工具中按住 Option 可临时切换到吸管。Shift 约束形状/移动方向或加选；Option 减选或从中心绘制。Command 拖动可移动选中像素，Command-Option 拖动可复制。Option 拖动可复制图层/文件夹/效果；Option 单击图层分界线可切换剪贴蒙版。Command 单击缩览图可载入其选区。Control 可绕过对齐。右击拖动可调整画笔大小。修饰键与鼠标的组合手势固定不变。",
})

# ---------------------------------------------------------------- 滤镜面板
ZH.update({
    "Tint": "色调",
    "Color the result while keeping its tones, for a sepia or a cyanotype":
        "在保留明暗层次的前提下着色，可做出棕褐色或蓝晒效果",
    "Shadows": "阴影",
    "Midtones": "中间调",
    "Highlights": "高光",
    "Preserve Luminosity": "保持明度",
    "Put each pixel's brightness back afterwards, so only the color moves":
        "之后还原每个像素的明度，只让颜色发生变化",
    "Hide the background behind a layer mask, keeping the foreground subjects. The pixels stay, so the background can be painted back at any time.":
        "用图层蒙版隐藏背景、保留前景主体。像素依然保留，随时可以把背景涂回来。",
    "Basic is quick; Advanced refines the mask against the layer's own detail, for hair and fur":
        "基础模式速度快；高级模式结合图层自身细节精修蒙版，适合头发与毛发",
    "Pull the mask onto the image's own edges, which recovers hair and fur":
        "让蒙版贴合图像自身的边缘，可找回头发与毛发",
    "Clear the haze that leaves background showing through thin areas":
        "清除雾状残留，避免背景从稀薄区域透出",
    "Shrink the mask to drop the rim of background color around the subject, or grow it":
        "收缩蒙版可去掉主体周围残留的背景色边，或扩张蒙版",
    "Fill the selection using surrounding pixels from this layer.":
        "使用本图层周围的像素填充选区。",
    "Distribution": "分布",
    "Uniform": "均匀",
    "Gaussian": "高斯",
    "Monochromatic": "单色",
    "Choose the vignette color": "选择暗角颜色",
    "Blend the chosen color into the edges while keeping the center unchanged":
        "将所选颜色融入边缘，中心保持不变",
    "Protect bright areas near the edge": "保护靠近边缘的明亮区域",
    "Positive straightens lines that bow outward (barrel); negative, lines that bow inward (pincushion).":
        "正值校正向外凸出的线条（桶形畸变）；负值校正向内凹陷的线条（枕形畸变）。",
    "Make each dithered pixel this many pixels across, for a chunky old-screen look":
        "抖动后每个像素点的边长，营造复古粗颗粒屏幕效果",
    "The height of each line of characters": "每行字符的高度",
    "How far apart the screen's lines are": "扫描线之间的间距",
    "Light blooming around the lines, like a CRT's phosphors":
        "扫描线周围的光晕溢出，模拟 CRT 荧光粉",
    "Break the lines into glowing beads": "把扫描线打断成发光的小点",
    "Make the lines waver sideways down the screen, like a CRT losing sync":
        "让扫描线沿屏幕左右抖动，如同 CRT 失去同步",
    "Characters": "字符",
    "The characters to draw with, in any order: each spot gets the one whose ink best matches its tone":
        "用于绘制的字符，顺序不限：每个位置使用墨色最接近该处明暗的字符",
    "Tones per channel: 2 is pure black and white": "每通道的色调数量：2 为纯黑白",
    "How much of each pixel's error spreads to its neighbors. Less gives flatter areas":
        "每个像素的误差向邻近像素扩散的比例。数值越小画面越平",
    "More ink (darker) or less before dithering": "抖动前增加墨量（变暗）或减少墨量",
    "Dark": "深色",
    "Light": "浅色",
    "Pixel Shape": "像素形状",
    "Draw each chunky pixel as a solid square, or as a round dot like a dot-matrix screen":
        "把每个粗像素画成实心方块，或像点阵屏那样画成圆点",
    "Light on Dark": "深底浅字",
    "Draw the marks for the light tones on the dark color, like a glowing screen":
        "在深色底上绘制浅色调的标记，如同发光屏幕",
    "Choose the \\(title.lowercased()) color": "选择\\(title.lowercased())颜色",
    "\\(title) color": "\\(title) 颜色",
})

# ---------------------------------------------------------------- Camera Raw
ZH.update({
    "Histogram": "直方图",
    "Vectorscope": "矢量示波器",
    "Red, green, and blue of the pixel under the pointer.": "指针所指像素的红、绿、蓝数值。",
    "White Balance": "白平衡",
    "Auto balances the average color. Custom follows Temperature and Tint.":
        "自动以平均颜色为基准校正。自定则跟随色温与色调。",
    "Click a pixel that should be neutral.": "单击画面中应为中性灰的像素。",
    "White Balance Selector": "白平衡选择器",
    "Click the original layer. Click the eyedropper again to stop.":
        "在原始图层上单击。再次单击吸管可退出。",
    "Glow": "辉光",
    "Diffusion is soft and wide, Bloom is tighter, and Halation is a red fringe.":
        "漫射柔和宽广，泛光更集中，光晕带红色边缘。",
    "Vignette": "晕影",
    "Highlight Priority protects bright edges. Color Priority also reduces color. Paint Overlay covers the edges evenly.":
        "高光优先保护明亮边缘。颜色优先同时降低饱和度。叠加绘制则均匀覆盖边缘。",
    "Grain": "颗粒",
    "Curve": "曲线",
    "Parametric lifts tonal regions. Point places anchors on the curve.":
        "参数式用于抬升各个色调区域。点式则在曲线上放置锚点。",
    "Channel": "通道",
    "RGB changes brightness. Red, green, and blue also shift the color.":
        "RGB 改变明度。红、绿、蓝同时会改变颜色。",
    "In \\(Int((point.x * 255).rounded()))   Out \\(Int((point.y * 255).rounded()))":
        "输入 \\(Int((point.x * 255).rounded()))   输出 \\(Int((point.y * 255).rounded()))",
    "Input and output of the selected curve point.": "所选曲线控制点的输入与输出值。",
    "Preset": "预设",
    "Linear": "线性",
    "Medium Contrast": "中等对比度",
    "Strong Contrast": "强对比度",
    "Replaces this curve with a straight line or a contrast curve.":
        "用直线或对比曲线替换当前曲线。",
    "Targeted Adjustment": "目标调整",
    "Mixer": "混合器",
    "HSL lists every color. Color edits one family. Point Color adjusts a color you pick.":
        "HSL 列出所有颜色。颜色模式编辑单一色系。点颜色则调整你选取的颜色。",
    "Component": "分量",
    "Hue shifts the color, Saturation its strength, and Luminance its brightness.":
        "色相改变颜色，饱和度改变浓度，明度改变亮暗。",
    "Drag a color in the picture. Nearby color families move together.":
        "在画面中拖动某个颜色。相邻色系会一起移动。",
    "Edit \\(CameraRawMixerSettings.names[index]).": "编辑 \\(CameraRawMixerSettings.names[index])。",
    "Click the picture to save a color. Up to eight colors.": "在画面上单击以保存颜色，最多八个。",
    "Select this picked color.": "选择这个取样颜色。",
    "Visualize Range": "显示范围",
    "Dims the picture outside this color's range. It is not kept when you press OK.":
        "压暗画面中该颜色范围以外的区域。按「确定」后不会保留。",
    "Grading": "颜色分级",
    "Three-Way shows shadows, midtones, and highlights. The other choices show one wheel.":
        "三向显示阴影、中间调与高光。其他选项只显示一个色轮。",
    "Drag inside the wheel. Angle sets hue, distance sets saturation.":
        "在色轮内拖动。角度决定色相，离中心的距离决定饱和度。",
    "Hue and saturation of this wheel.": "该色轮的色相与饱和度。",
    "Drag to set hue and saturation. Double-click to reset this wheel.":
        "拖动可设置色相与饱和度。双击可复位该色轮。",
    "Sharpening": "锐化",
    "Noise Reduction": "降噪",
    "Remove Chromatic Aberration": "移去色差",
    "Pulls red and blue fringes apart toward the center to reduce color edging.":
        "把红、蓝色边朝中心分开，减少彩色镶边。",
    "Enable Lens Profile Corrections": "启用镜头配置文件校正",
    "Applies generic profile strength when camera metadata is not available.":
        "相机元数据不可用时，应用通用配置文件强度。",
    "No lens metadata on this layer. Profile sliders set generic correction strength.":
        "该图层没有镜头元数据。配置文件滑块用于设置通用校正强度。",
    "Manual": "手动",
    "Defringe": "去边",
    "Click a purple or green fringe to set its hue range.": "单击紫色或绿色边缘以设置其色相范围。",
    "Click the fringe on the layer. Click the eyedropper again to stop.":
        "在图层上单击彩色边缘。再次单击吸管可退出。",
    "Low": "低",
    "Start of the hue range, in degrees.": "色相范围的起点（度）。",
    "High": "高",
    "End of the hue range, in degrees.": "色相范围的终点（度）。",
    "Upright": "自动校正",
    "Off leaves the picture as it is. Guided straightens from lines you draw on the picture.":
        "关闭则保持原样。引导式根据你在画面上绘制的线条进行校正。",
    "Draw Guides": "绘制参考线",
    "Draw two or more lines on the preview that should be level or vertical.":
        "在预览上绘制两条以上本应水平或垂直的线条。",
    "Drag on the layer to place a guide. Draw at least two lines.":
        "在图层上拖动可放置参考线。请至少绘制两条。",
    "Remove every guide line.": "移除所有参考线。",
    "Projection": "投影",
    "Perspective allows stronger keystone. Rectilinear keeps the warp gentler.":
        "透视允许更强的梯形校正。直线投影的变形更缓和。",
    "Constrain Crop": "约束裁剪",
    "Crops empty edges after the transform and fits the result back into the frame.":
        "变换后裁掉空白边缘，并把结果重新适配回画面内。",
    "Process": "处理",
    "Chooses how strongly the calibration sliders below are applied. Version 6 is the current default.":
        "决定下方校正滑块的生效强度。版本 6 为当前默认值。",
    "Red Primary": "红原色",
    "Green Primary": "绿原色",
    "Blue Primary": "蓝原色",
})

# ---------------------------------------------------------------- 枚举显示名 / 工具 / 菜单项
ZH.update({
    # NavigationTool 的工具提示
    "Type (T)": "文字 (T)",
    "Eyedropper (I)": "吸管 (I)",
    "Marquee (M)": "选框 (M)",
    "Lasso (L)": "套索 (L)",
    "Magic (W) · Tab switches Wand and Object": "魔棒 (W) · 按 Tab 切换魔棒与对象",
    "Brush (B) · Eraser (E)": "画笔 (B) · 橡皮擦 (E)",
    "Spot Healing Brush (J)": "污点修复画笔 (J)",
    "Clone Stamp (S) · Option-click sets the source": "仿制图章 (S) · 按住 Option 单击设置取样点",
    "Smear (R)": "涂抹 (R)",
    "Gradient (G)": "渐变 (G)",
    "Shape (U) · Shift-U switches Rectangle/Ellipse": "形状 (U) · Shift-U 切换矩形/椭圆",
    "Crop (C)": "裁剪 (C)",
    "Move / Transform (V)": "移动/变换 (V)",
    "Hand (H)": "抓手 (H)",
    "Zoom (Z)": "缩放 (Z)",
    "Move / Transform": "移动/变换",
    "Rectangular Marquee": "矩形选框",
    "Elliptical Marquee": "椭圆选框",
    "Polygonal Lasso": "多边形套索",
    "Magic Wand": "魔棒",
    "Object Selection": "对象选择",
    "Eraser": "橡皮擦",
    "Spot Healing Brush": "污点修复画笔",
    "Clone Stamp": "仿制图章",
    "Liquify": "液化",
    "Blur": "模糊",
    "Smudge": "涂抹",
    "Hand": "抓手",
    "Zoom": "缩放",
    "Type": "文字",
    "Brush": "画笔",
    "Tool › ": "工具 › ",
    "Layer › ": "图层 › ",
    "Layer › Add Layer Mask": "图层 › 添加图层蒙版",
    "Layer › Add Layer Mask from Selection": "图层 › 从选区添加图层蒙版",
    "Layer › Add Layer Mask (Hide All)": "图层 › 添加图层蒙版（隐藏全部）",
    "Layer › Add Layer Mask Hiding Selection": "图层 › 添加隐藏选区的图层蒙版",

    # 图层面板的 AppKit 菜单项
    "Duplicate Layer": "复制图层",
    "Rename…": "重命名…",
    "Delete Mask": "删除蒙版",
    "Delete Selected Layers": "删除所选图层",
    "Delete Layer": "删除图层",
    "Release Clipping Mask": "释放剪贴蒙版",
    "Create Clipping Mask": "创建剪贴蒙版",
    "Merge Down": "向下合并",
    "Add Mask": "添加蒙版",
    "Reveal All (White)": "显示全部（白色）",
    "Hide All (Black)": "隐藏全部（黑色）",
    "Enable Mask": "启用蒙版",
    "Disable Mask": "停用蒙版",
    "Link Mask": "链接蒙版",
    "Unlink Mask": "取消链接蒙版",
    "Show Layer": "显示图层",
    "Hide Layer": "隐藏图层",
    "Export PNG": "导出 PNG",

    # 图标调色板 / 其他 AppKit 提示
    "Multiple": "多种",

    # —— 枚举显示值 ——
    # SpotHealingMode
    "Content-Aware": "内容识别",
    "Create Texture": "生成纹理",
    "Proximity Match": "邻近匹配",
    # CameraRawWhiteBalance
    "Auto": "自动",
    "Custom": "自定",
    # CameraRawGlowStyle
    "Diffusion": "漫射",
    "Bloom": "泛光",
    "Halation": "光晕",
    # CameraRawVignetteStyle
    "Highlight Priority": "高光优先",
    "Color Priority": "颜色优先",
    "Paint Overlay": "叠加绘制",
    # CameraRawScopeMode
    "Dither": "抖动",
    # CameraRawCurvePage / MixerPage / MixerTab / GradePage
    "Parametric": "参数式",
    "Point": "点式",
    "Point Color": "点颜色",
    "Three-Way": "三向",
    "Global": "全局",
    "HSL": "HSL",
    "Luminance": "明度",
    # CameraRawUprightMode / Projection
    "Off": "关闭",
    "Guided": "引导式",
    "Perspective": "透视",
    "Rectilinear": "直线",
    # CameraRawProcessVersion
    "Version 1": "版本 1",
    "Version 2": "版本 2",
    "Version 3": "版本 3",
    "Version 4": "版本 4",
    "Version 5": "版本 5",
    "Version 6": "版本 6",
    # CanvasUnit
    "Pixels": "像素",
    "Percent": "百分比",
    "Inches": "英寸",
    "Centimeters": "厘米",
    # DitherStyle
    "Atkinson (Classic Mac)": "Atkinson（经典 Mac）",
    "Halftone Dots": "半调网点",
    "Halftone Lines": "半调线",
    "Halftone Diamonds": "半调菱形",
    "Mac Patterns": "Mac 图案",
    "Scanlines (CRT)": "扫描线 (CRT)",
    # DitherPixelShape / DitherColors
    "Square": "方形",
    "Dot": "圆点",
    "Black & White": "黑白",
    "Two Colors": "双色",
    "Original": "原始",
    # FilterKind
    "Gaussian Blur": "高斯模糊",
    "Motion Blur": "动感模糊",
    "Add Noise": "添加杂色",
    "Vignette": "晕影",
    "Bloom / Glow": "泛光/辉光",
    "Tonal Contrast": "色调对比度",
    "Lens Correction": "镜头校正",
    "Camera Raw Filter": "Camera Raw 滤镜",
    "Remove Background": "移除背景",
    "Content-Aware Fill": "内容识别填充",
    "Curves": "曲线",
    "Exposure": "曝光",
    "Gradient Map": "渐变映射",
    "Grain": "颗粒",
    "Color Balance": "色彩平衡",
    # BackgroundQuality
    "Basic": "基础",
    "Advanced": "高级",
    # GradientStyle / GradientShape
    "Foreground to Background": "前景色到背景色",
    "Foreground to Transparent": "前景色到透明",
    "Linear": "线性",
    "Radial": "径向",
    # Guides 预设颜色与样式
    "Light Gray": "浅灰",
    "Light Blue": "浅蓝",
    "Light Red": "浅红",
    "Green": "绿色",
    "Medium Blue": "中蓝",
    "Yellow": "黄色",
    "Magenta": "洋红",
    "Cyan": "青色",
    "Black": "黑色",
    "Lines": "实线",
    "Dashed Lines": "虚线",
    "Dots": "点线",
    # 色相/饱和度：颜色范围
    "Master": "全图",
    "Reds": "红色",
    "Oranges": "橙色",
    "Yellows": "黄色",
    "Greens": "绿色",
    "Cyans": "青色",
    "Blues": "蓝色",
    "Purples": "紫色",
    "Magentas": "洋红",
    "Aquas": "青色",
    # Levels / Camera Raw 通道
    "RGB": "RGB",
    "Red": "红色",
    "Blue": "蓝色",
    # HueSampleMode
    "Add": "添加",
    "Subtract": "减去",
    "Remove": "减去",
    # AdjustmentKind
    "Hue/Saturation": "色相/饱和度",
    "Levels": "色阶",
    "Invert": "反相",
    # LayerBlendMode
    "Normal": "正常",
    "Darken": "变暗",
    "Multiply": "正片叠底",
    "Color Burn": "颜色加深",
    "Linear Burn": "线性加深",
    "Lighten": "变亮",
    "Screen": "滤色",
    "Color Dodge": "颜色减淡",
    "Linear Dodge (Add)": "线性减淡（添加）",
    "Overlay": "叠加",
    "Soft Light": "柔光",
    "Hard Light": "强光",
    "Vivid Light": "亮光",
    "Linear Light": "线性光",
    "Pin Light": "点光",
    "Hard Mix": "实色混合",
    "Difference": "差值",
    "Exclusion": "排除",
    "Divide": "划分",
    "Hue": "色相",
    "Saturation": "饱和度",
    "Luminosity": "明度",
    # LayerSampling
    "Nearest": "邻近",
    "Smooth": "平滑",
    "High quality": "高品质",
    # LevelsAuto
    "Contrast": "对比度",
    "Color + neutral midtones": "颜色 + 中性中间调",
    # 选区
    "Wand": "魔棒",
    "Object": "对象",
    "Freehand": "手绘",
    "Polygonal": "多边形",
    "Rectangle": "矩形",
    "Ellipse": "椭圆",
    "Line": "直线",
    "New": "新建",
    "Expand": "扩展",
    "Contract": "收缩",
    # 画笔 / 涂抹
    "Paint": "绘画",
    "Erase": "擦除",
    # 文字对齐（"Left"/"Right" 与裁切方向同形，走定向替换，这里只留 "Center"）
    "Center": "居中",
    # 新增画布预设（"Custom" 见上）
    "Square canvas": "正方形画布",
})

# ---------------------------------------------------------------- 带插值的文案（需逐字符匹配）
ZH.update({
    "Current: \\(draft.originalWidth) × \\(draft.originalHeight) pixels":
        "当前：\\(draft.originalWidth) × \\(draft.originalHeight) 像素",
    "\\(bytes(draft.originalWidth, draft.originalHeight)) uncompressed RGBA canvas":
        "\\(bytes(draft.originalWidth, draft.originalHeight)) 未压缩 RGBA 画布",
    "New: \\(Int(draft.width.rounded())) × \\(Int(draft.height.rounded())) pixels · \\(bytes(Int(draft.width.rounded()), Int(draft.height.rounded()))) uncompressed":
        "新：\\(Int(draft.width.rounded())) × \\(Int(draft.height.rounded())) 像素 · \\(bytes(Int(draft.width.rounded()), Int(draft.height.rounded()))) 未压缩",
    "Final dimensions must be 1–\\(DocumentLimits.maxSide.formatted()) pixels per side.":
        "最终尺寸每边必须为 1–\\(DocumentLimits.maxSide.formatted()) 像素。",
    "\\(mode.rawValue) color": "\\(mode.rawValue)颜色",
    "Current: \\(document.width) × \\(document.height) pixels":
        "当前：\\(document.width) × \\(document.height) 像素",
    "\\(title) the selection by this many pixels": "将选区\\(title)此像素数",
    "Original \\(settings.channel.rawValue) histogram": "原始\\(settings.channel.rawValue)直方图",
    "Edit \\(original.kind.rawValue) Adjustment": "编辑\\(original.kind.rawValue)调整",
    "New \\(kind.rawValue) Adjustment": "新建\\(kind.rawValue)调整",
    "Layer \\(number)": "图层 \\(number)",
    "Layer 1": "图层 1",
    "Folder \\(number)": "文件夹 \\(number)",
    "Untitled \\(nextNumber)": "未命名 \\(nextNumber)",
    "Open “\\(url.lastPathComponent)”?": "打开“\\(url.lastPathComponent)”？",
})

# ---------------------------------------------------------------- 数组型选项与零散文案
ZH.update({
    # 画布扩展颜色
    "Transparent": "透明",
    "Foreground": "前景色",
    "White": "白色",
    "Gray": "灰色",
    "Extension Color": "扩展颜色",
    "Selected": "已选中",
    # 画布定位九宫格
    "Top left": "左上",
    "Top center": "上中",
    "Top right": "右上",
    "Middle left": "左中",
    "Middle right": "右中",
    "Bottom left": "左下",
    "Bottom center": "下中",
    "Bottom right": "右下",
    # 裁剪比例
    "Free": "自由",
    # 色阶输入 / 输出端点
    "Input black": "输入黑场",
    "Gamma": "灰度系数",
    "Input white": "输入白场",
    "Output black": "输出黑场",
    "Output white": "输出白场",
    # 快捷键面板分组
    "Menus": "菜单",
    "Canvas & Layers": "画布与图层",
    "Text Editing": "文本编辑",
})

# ---------------------------------------------------------------- 底部提示条 / 快捷键条目 / 收尾
ZH.update({
    # 图层面板空态
    "Create a canvas or import an image.": "创建画布或导入图像。",
    "Import an image or add a blank layer.": "导入图像或新建空白图层。",

    # 底部工具提示条
    "Drag an ellipse · Shift add · Option subtract · Shift again mid-drag circle · Drag inside to move · Delete clears · ⌘D deselect":
        "拖出椭圆 · Shift 加选 · Option 减选 · 拖动中再按 Shift 变正圆 · 在选区内拖动可移动 · Delete 清除 · ⌘D 取消选择",
    "Drag a rectangle · Shift add · Option subtract · Shift again mid-drag square · Drag inside to move · ⌘-drag moves pixels · Delete clears · ⌘D deselect":
        "拖出矩形 · Shift 加选 · Option 减选 · 拖动中再按 Shift 变正方形 · 在选区内拖动可移动 · ⌘ 拖动移动像素 · Delete 清除 · ⌘D 取消选择",
    "Click an object to select its outline · Tab for Wand · Shift add · Option subtract · Drag inside to move · ⌘-drag moves pixels · Delete clears · ⌘D deselect":
        "单击对象即可选中其轮廓 · 按 Tab 切换魔棒 · Shift 加选 · Option 减选 · 在选区内拖动可移动 · ⌘ 拖动移动像素 · Delete 清除 · ⌘D 取消选择",
    "Click to select similar colors · Tab for Object · Shift add · Option subtract · Drag inside to move · ⌘-drag moves pixels · Delete clears · ⌘D deselect":
        "单击选择相似颜色 · 按 Tab 切换对象 · Shift 加选 · Option 减选 · 在选区内拖动可移动 · ⌘ 拖动移动像素 · Delete 清除 · ⌘D 取消选择",
    "Drag to select · Drag inside to move · Shift add · Option subtract · Delete clears · ⌥⌫/⌘⌫ fill · ⌘D deselect":
        "拖动以选择 · 在选区内拖动可移动 · Shift 加选 · Option 减选 · Delete 清除 · ⌥⌫/⌘⌫ 填充 · ⌘D 取消选择",
    "Click corners · Click start, double-click or Enter to close · Delete removes corner · Escape cancel":
        "单击各角点 · 单击起点后双击或按 Enter 闭合 · Delete 移除角点 · Esc 取消",
    "Drag to erase": "拖动以擦除",
    "Drag to paint": "拖动以绘画",
    " · [ ] size · Shift-[ ] hardness · 1–0 opacity · Escape cancel · Space to pan":
        " · [ ] 大小 · Shift-[ ] 硬度 · 1–0 不透明度 · Esc 取消 · 空格平移",
    "Drag to soften": "拖动以柔化",
    "Drag to smudge": "拖动以涂抹",
    "Drag to push pixels": "拖动以推移像素",
    " · [ ] size · Shift-[ ] hardness · 1–0 strength · Space to pan":
        " · [ ] 大小 · Shift-[ ] 硬度 · 1–0 强度 · 空格平移",
    "Option-click to set the source · Drag to clone · [ ] size · Shift-[ ] hardness · 1–0 opacity · Space to pan":
        "Option 单击设置取样点 · 拖动以仿制 · [ ] 大小 · Shift-[ ] 硬度 · 1–0 不透明度 · 空格平移",
    "Drag over blemishes to heal · [ ] size · Shift-[ ] hardness · Escape cancel · Space to pan":
        "在瑕疵上拖动即可修复 · [ ] 大小 · Shift-[ ] 硬度 · Esc 取消 · 空格平移",
    "Drag a text box · Click text to edit · Drag box handles to resize · ⌘Return finish · Escape cancel":
        "拖出文本框 · 单击文字可编辑 · 拖动边角可调整大小 · ⌘Return 完成 · Esc 取消",
    "Drag to draw a shape on a new layer · Shift \\(session.shapeKind == .line ? \"45°\" : session.shapeKind == .rectangle ? \"square\" : \"circle\") · Option from center · Shift-U or Tab for the next shape · Escape cancel · Space to pan":
        "在新图层上拖动画出形状 · Shift \\(session.shapeKind == .line ? \"45°\" : session.shapeKind == .rectangle ? \"正方形\" : \"圆形\") · Option 从中心绘制 · Shift-U 或 Tab 切换形状 · Esc 取消 · 空格平移",
    "Drag to draw · Drag ends to adjust · Shift 45° · 1–0 opacity · Enter apply · Escape cancel":
        "拖动绘制 · 拖动端点可调整 · Shift 锁定 45° · 1–0 不透明度 · Enter 应用 · Esc 取消",
    "Drag to crop · Enter apply · Escape cancel · Space to pan":
        "拖动出裁剪框 · Enter 应用 · Esc 取消 · 空格平移",
    "Drag to move · Handles to resize · Circle to rotate · 1–0 layer opacity · Space to pan":
        "拖动移动 · 拖动控制点缩放 · 拖动圆圈旋转 · 1–0 图层不透明度 · 空格平移",
    "Drag to pan · Pinch to zoom": "拖动平移 · 捏合缩放",
    "No tool selected · Press a tool's key to pick one · Space to pan":
        "未选择工具 · 按工具快捷键即可选择 · 空格平移",
    "Click to zoom in · Option-click to zoom out · Drag right or left to zoom smoothly · Space to pan":
        "单击放大 · Option 单击缩小 · 左右拖动平滑缩放 · 空格平移",

    # 快捷键列表条目
    "Open Project": "打开项目",
    "Save As": "存储为",
    "Command Palette": "命令面板",
    "Fill with Foreground": "填充前景色",
    "Fill with Background": "填充背景色",
    "Select All": "全选",
    "Inverse Selection": "反选",
    "Invert Pixels / Mask": "反相像素/蒙版",
    "Transform Layer / Selection": "变换图层/选区",
    "Duplicate / Layer via Copy": "复制/通过拷贝的图层",
    "Toggle Clipping Mask": "切换剪贴蒙版",
    "Merge Layers": "合并图层",
    "Show Grid": "显示网格",
    "Show Guides": "显示参考线",
    "Show Rulers": "显示标尺",
    "Canvas Only: full screen on black, without panels": "仅显示画布：全屏黑底，隐藏面板",
    "Select tool": "选择工具",
    "Move / Transform tool": "移动/变换工具",
    "Hand tool": "抓手工具",
    "Zoom tool": "缩放工具",
    "Brush tool": "画笔工具",
    "Spot Healing": "污点修复",
    "Type tool": "文字工具",
    "Gradient tool": "渐变工具",
    "Shape tool": "形状工具",
    "Eyedropper tool": "吸管工具",
    "Marquee / cycle shape": "选框/切换形状",
    "Magic": "魔棒",
    "Lasso / cycle mode": "套索/切换模式",
    "Blur / Smudge / Liquify": "模糊/涂抹/液化",
    "Crop tool": "裁剪工具",
    "Swap foreground/background": "切换前景/背景色",
    "Reset colors": "复位颜色",
    "Cycle tool mode": "切换工具模式",
    "Temporary Hand tool (hold)": "临时抓手（按住）",
    "Delete selection / layer / effect / lasso point": "删除选区/图层/效果/套索点",
    "Apply current canvas operation": "应用当前画布操作",
    "Cancel current canvas operation": "取消当前画布操作",
    "Decrease brush size": "减小画笔",
    "Increase brush size": "增大画笔",
    "Decrease brush hardness": "减小画笔硬度",
    "Increase brush hardness": "增大画笔硬度",
    "Previous blend mode": "上一个混合模式",
    "Next blend mode": "下一个混合模式",
    "Cycle shape kind": "切换形状",
    "Opacity digit \\(digit) (type two for exact %)": "不透明度数字 \\(digit)（连输两位可精确到 %）",
    "Up": "上",
    "Down": "下",
    "Nudge \\(direction) 1 px": "微调 \\(direction) 1 px",
    "Nudge \\(direction) 10 px": "微调 \\(direction) 10 px",
    "Move selected pixels \\(direction) 1 px": "移动所选像素 \\(direction) 1 px",
    "Move selected pixels \\(direction) 10 px": "移动所选像素 \\(direction) 10 px",
    "Finish editing text": "完成文字编辑",
    "Decrease tracking": "减小字距",
    "Increase tracking": "增大字距",
    "Decrease leading": "减小行距",
    "Increase leading": "增大行距",
    " by 10": "（×10）",
    "Toggle Levels preview": "切换色阶预览",
})




# ---------------------------------------------------------------- 撤销菜单 / 自动命名 / 分组标题
ZH.update({
    # 编辑 > 撤销 的名称
    "Clear": "清除",
    "Copy Layers from Project": "从项目复制图层",
    "Delete Guide": "删除参考线",
    "Delete Layer Mask": "删除图层蒙版",
    "Delete Layers": "删除图层",
    "Distort Layer Mask": "扭曲图层蒙版",
    "Fill Text": "填充文字",
    "Group Layers": "编组图层",
    "Import Image": "导入图像",
    "Import Photoshop File": "导入 Photoshop 文件",
    "Layer Blend Mode": "图层混合模式",
    "Layer Opacity": "图层不透明度",
    "Move Guide": "移动参考线",
    "Move Layer": "移动图层",
    "Move Selection": "移动选区",
    "New Canvas": "新建画布",
    "New Folder": "新建文件夹",
    "New Guide": "新建参考线",
    "Rename Layer": "重命名图层",
    "Reorder Layers": "重排图层",
    "Transform Layer": "变换图层",
    "Transform Layer Mask": "变换图层蒙版",
    "Transform Layers": "变换多个图层",
    "Transform Selection": "变换选区",
    "Layer via Copy": "通过拷贝的图层",
    "New Text Layer": "新建文字图层",

    # 自动命名
    "Select Subject": "选择主体",
    "Load Layer Selection": "载入图层选区",
    "Load Mask Selection": "载入蒙版选区",
    "Contract Selection": "收缩选区",
    "Expand Selection": "扩展选区",
    "Feather Selection": "羽化选区",
    "Floating Selection": "浮动选区",
    "Adjustment input": "调整输入",
    "Canvas Extension": "画布扩展",
    "Background": "背景",
    "Untitled": "未命名",
    "Tip": "提示",

    # Camera Raw 面板的分组标题（"Light" 在滤镜里另有含义，走定向替换）
    "Effects": "效果",
    "Color Mixer": "颜色混合器",
    "Color Grading": "颜色分级",
    "Detail": "细节",
    "Optics": "光学",
    "Geometry": "几何",
    "Calibration": "校准",

    # 魔棒取样大小
    "Point Sample": "单点取样",
    "3 by 3 Average": "3 × 3 平均",
    "5 by 5 Average": "5 × 5 平均",

    # 位置名称
    "Layer Mask": "图层蒙版",
})




