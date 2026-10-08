import AppKit
import SwiftUI

/// Camera Raw Filter's adjustment column: the histogram, then Light, Color, Color Grading, Effects, Curve,
/// Color Mixer, Detail, Optics, Geometry, and Calibration.
@MainActor
struct CameraRawControls: View {
    @Bindable var session: EditorSession
    @State private var expanded: Set<Section> = [.light, .color, .colorGrading]
    @State private var optionMonitor: Any?

    private var settings: FilterSettings { session.filterEdit?.settings ?? FilterSettings() }
    private var raw: CameraRawSettings { settings.cameraRaw }

    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            histogram
            ScrollView {
                VStack(alignment: .leading, spacing: 12) {
                    ForEach(Section.allCases) { section in
                        disclosure(section)
                    }
                }
                .frame(maxWidth: .infinity, alignment: .leading)
            }
            .frame(maxHeight: .infinity)
        }
        .frame(maxHeight: .infinity, alignment: .top)
        .onAppear { installOptionMonitor() }
        .onDisappear { removeOptionMonitor() }
    }

    private var histogram: some View {
        let scope = session.filterEdit?.cameraRawScope
        let mode = session.filterEdit?.cameraRawScopeMode ?? .histogram
        return VStack(alignment: .leading, spacing: 4) {
            ZStack {
                graph(scope, mode: mode)
                    .frame(height: 110)
                    .background(Color.black.opacity(0.35))
                    .clipShape(RoundedRectangle(cornerRadius: 4, style: .continuous))
                HStack {
                    clipButton(shadows: true)
                    Spacer()
                    clipButton(shadows: false)
                }
                .padding(4)
            }
            .contextMenu {
                Button("直方图") { session.filterEdit?.cameraRawScopeMode = .histogram }
                Button("矢量示波器") { session.filterEdit?.cameraRawScopeMode = .vectorscope }
            }
            .help(mode == .histogram
                  ? "Tones from black on the left to white on the right: blacks, shadows, midtones, highlights, whites. Control-click to show the vectorscope."
                  : "Hue around the wheel, saturation outward from the center. Control-click to show the histogram.")
            Text(readout)
                .font(.caption.monospacedDigit())
                .foregroundStyle(.secondary)
                .help("指针所指像素的红、绿、蓝数值。")
        }
    }

    private var readout: String {
        guard let value = session.filterEdit?.cameraRawReadout else { return "R —   G —   B —" }
        return "R \(value.red)   G \(value.green)   B \(value.blue)"
    }

    private func clipButton(shadows: Bool) -> some View {
        let on = shadows ? session.filterEdit?.showsShadowClipping == true : session.filterEdit?.showsHighlightClipping == true
        return Button {
            if shadows { session.filterEdit?.showsShadowClipping.toggle() }
            else { session.filterEdit?.showsHighlightClipping.toggle() }
            if let edit = session.filterEdit { session.updateFilter(edit.settings, preview: edit.preview) }
        } label: {
            Image(systemName: "triangle.fill")
                .font(.caption2)
                .foregroundStyle(on ? (shadows ? Color.blue : Color.red) : Color.white.opacity(0.55))
        }
        .buttonStyle(.plain)
        .help(shadows ? "Show clipped shadows in blue on the preview." : "Show clipped highlights in red on the preview.")
        .accessibilityLabel(shadows ? "Shadow Clipping Indicator" : "Highlight Clipping Indicator")
    }

    private func graph(_ scope: CameraRawScope?, mode: CameraRawScopeMode) -> some View {
        Canvas { context, size in
            guard let scope else { return }
            switch mode {
            case .histogram:
                let peak = scope.peak
                guard peak > 0 else { return }
                ribbon(scope.red, color: .red, peak: peak, in: context, size: size)
                ribbon(scope.green, color: .green, peak: peak, in: context, size: size)
                ribbon(scope.blue, color: .blue, peak: peak, in: context, size: size)
            case .vectorscope:
                let peak = scope.vectorscope.max() ?? 0
                guard peak > 0 else { return }
                let cell = size.width / CGFloat(CameraRawScope.scopeSide)
                for index in scope.vectorscope.indices where scope.vectorscope[index] > 0 {
                    let column = index % CameraRawScope.scopeSide
                    let row = index / CameraRawScope.scopeSide
                    let amount = min(1, scope.vectorscope[index] / peak)
                    let rect = CGRect(x: CGFloat(column) * cell, y: size.height - CGFloat(row + 1) * cell, width: cell + 0.2, height: cell + 0.2)
                    context.fill(Path(rect), with: .color(.white.opacity(0.15 + 0.85 * amount)))
                }
            }
        }
        .accessibilityLabel(mode == .histogram ? "RGB histogram" : "矢量示波器")
    }

    private func ribbon(_ bins: [Double], color: Color, peak: Double, in context: GraphicsContext, size: CGSize) {
        var path = Path()
        path.move(to: CGPoint(x: 0, y: size.height))
        for index in bins.indices {
            let x = CGFloat(index) * size.width / CGFloat(bins.count)
            let height = size.height * min(1, max(0, bins[index] / peak))
            path.addLine(to: CGPoint(x: x, y: size.height - height))
        }
        path.addLine(to: CGPoint(x: size.width, y: size.height))
        path.closeSubpath()
        context.fill(path, with: .color(color.opacity(0.55)))
    }

    @ViewBuilder private func disclosure(_ section: Section) -> some View {
        VStack(alignment: .leading, spacing: 8) {
            HStack(spacing: 6) {
                Button {
                    if expanded.contains(section) { expanded.remove(section) } else { expanded.insert(section) }
                } label: {
                    HStack(spacing: 6) {
                        Image(systemName: expanded.contains(section) ? "chevron.down" : "chevron.right")
                            .font(.caption.weight(.semibold))
                            .frame(width: 12)
                        Text(section.rawValue).font(.headline)
                    }
                    .contentShape(Rectangle())
                }
                .buttonStyle(.plain)
                .accessibilityLabel(section.rawValue)
                Spacer(minLength: 0)
                if section == .light, raw.adjustsLight { eye(shown: session.filterEdit?.showsCameraRawLight ?? true, name: "光线", group: .light) }
                if section == .color, raw.adjustsColor { eye(shown: session.filterEdit?.showsCameraRawColor ?? true, name: "颜色", group: .color) }
                if section == .effects, raw.adjustsEffects { eye(shown: session.filterEdit?.showsCameraRawEffects ?? true, name: "效果", group: .effects) }
                if section == .curve, raw.adjustsCurve { eye(shown: session.filterEdit?.showsCameraRawCurve ?? true, name: "曲线", group: .curve) }
                if section == .colorMixer, raw.adjustsMixer { eye(shown: session.filterEdit?.showsCameraRawMixer ?? true, name: "颜色混合器", group: .mixer) }
                if section == .colorGrading, raw.adjustsGrading { eye(shown: session.filterEdit?.showsCameraRawGrading ?? true, name: "颜色分级", group: .grading) }
                if section == .detail, raw.adjustsDetail { eye(shown: session.filterEdit?.showsCameraRawDetail ?? true, name: "细节", group: .detail) }
                if section == .optics, raw.adjustsOptics { eye(shown: session.filterEdit?.showsCameraRawOptics ?? true, name: "光学", group: .optics) }
                if section == .geometry, raw.adjustsGeometry { eye(shown: session.filterEdit?.showsCameraRawGeometry ?? true, name: "几何", group: .geometry) }
                if section == .calibration, raw.adjustsCalibration { eye(shown: session.filterEdit?.showsCameraRawCalibration ?? true, name: "校准", group: .calibration) }
            }
            if expanded.contains(section) {
                switch section {
                case .light: lightControls.padding(.leading, 18)
                case .color: colorControls.padding(.leading, 18)
                case .effects: effectsControls.padding(.leading, 18)
                case .curve: CameraRawCurveControls(session: session).padding(.leading, 18)
                case .colorMixer: CameraRawMixerControls(session: session).padding(.leading, 18)
                case .colorGrading: CameraRawGradingControls(session: session).padding(.leading, 18)
                case .detail: CameraRawDetailControls(session: session).padding(.leading, 18)
                case .optics: CameraRawOpticsControls(session: session).padding(.leading, 18)
                case .geometry: CameraRawGeometryControls(session: session).padding(.leading, 18)
                case .calibration: CameraRawCalibrationControls(session: session).padding(.leading, 18)
                }
            }
        }
    }

    private var lightControls: some View {
        VStack(alignment: .leading, spacing: 8) {
            slider("曝光", \.exposure, range: CameraRawSettings.exposureRange, decimals: 2, clipping: .highlights,
                   help: "Brightens or darkens the whole picture, in stops of light. Hold Option to see clipped highlights.")
            slider("对比度", \.contrast, range: CameraRawSettings.toneRange, decimals: 0, clipping: nil,
                   help: "Makes light and dark tones more or less different, mostly around the middle.")
            slider("高光", \.highlights, range: CameraRawSettings.toneRange, decimals: 0, clipping: .highlights,
                   help: "Adjusts the bright parts of the picture. Hold Option to see clipped highlights.")
            slider("阴影", \.shadows, range: CameraRawSettings.toneRange, decimals: 0, clipping: .shadows,
                   help: "Adjusts the dark parts of the picture. Hold Option to see clipped shadows.")
            slider("Whites", \.whites, range: CameraRawSettings.toneRange, decimals: 0, clipping: .highlights,
                   help: "Sets the brightest point. Hold Option to see clipped highlights.")
            slider("Blacks", \.blacks, range: CameraRawSettings.toneRange, decimals: 0, clipping: .shadows,
                   help: "Sets the darkest point. Hold Option to see clipped shadows.")
        }
    }

    private var colorControls: some View {
        VStack(alignment: .leading, spacing: 8) {
            HStack(spacing: 10) {
                Text("白平衡").frame(minWidth: Self.labelWidth, alignment: .leading)
                    .help("自动以平均颜色为基准校正。自定则跟随色温与色调。")
                Picker("白平衡", selection: Binding(get: { raw.whiteBalance }, set: setWhiteBalance)) {
                    ForEach(CameraRawWhiteBalance.allCases, id: \.self) { Text($0.rawValue).tag($0) }
                }
                .labelsHidden()
                .help("自动以平均颜色为基准校正。自定则跟随色温与色调。")
                Button {
                    session.filterEdit?.samplesWhiteBalance.toggle()
                    session.brushRevision += 1
                } label: {
                    Image(systemName: "eyedropper")
                }
                .buttonStyle(.borderless)
                .tint(session.filterEdit?.samplesWhiteBalance == true ? Color.accentColor : Color.secondary)
                .help("单击画面中应为中性灰的像素。")
                .accessibilityLabel("白平衡选择器")
            }
            if session.filterEdit?.samplesWhiteBalance == true {
                Text("在原始图层上单击。再次单击吸管可退出。")
                    .font(.caption).foregroundStyle(.secondary).fixedSize(horizontal: false, vertical: true)
            }
            slider("Temperature", \.temperature, range: CameraRawSettings.toneRange, decimals: 0, clipping: nil,
                   track: .temperature, help: "Shifts the picture from blue to yellow.")
            slider("色调", \.tint, range: CameraRawSettings.toneRange, decimals: 0, clipping: nil,
                   track: .tint, help: "Shifts the picture from green to mauve.")
            slider("Vibrance", \.vibrance, range: CameraRawSettings.toneRange, decimals: 0, clipping: nil,
                   track: .chroma, help: "Strengthens quiet colors more than colors that are already strong, and protects skin tones.")
            slider("饱和度", \.saturation, range: CameraRawSettings.toneRange, decimals: 0, clipping: nil,
                   track: .chroma, help: "Strengthens or weakens every color by the same amount.")
        }
    }

    private var effectsControls: some View {
        VStack(alignment: .leading, spacing: 8) {
            slider("Texture", \.texture, range: CameraRawSettings.toneRange, decimals: 0, clipping: nil,
                   help: "Adds or softens small detail.")
            slider("Clarity", \.clarity, range: CameraRawSettings.toneRange, decimals: 0, clipping: nil,
                   help: "Adds or softens contrast along broader shapes.")
            slider("Dehaze", \.dehaze, range: CameraRawSettings.toneRange, decimals: 0, clipping: nil,
                   help: "Clears haze when raised, and adds haze when lowered.")
            Text("辉光").font(.subheadline)
            slider("辉光", \.glow, range: CameraRawSettings.unitRange, decimals: 0, clipping: nil,
                   help: "Spreads a glow from the bright areas.")
            Picker("Style", selection: Binding(get: { raw.glowStyle }, set: { style in update { $0.cameraRaw.glowStyle = style } })) {
                ForEach(CameraRawGlowStyle.allCases, id: \.self) { Text($0.rawValue).tag($0) }
            }
            .help("漫射柔和宽广，泛光更集中，光晕带红色边缘。")
            VStack(alignment: .leading, spacing: 8) {
                slider("范围", \.glowRange, range: CameraRawSettings.toneRange, decimals: 0, clipping: nil,
                       help: "Chooses how bright an area must be to glow. Has no effect until Glow is raised.")
                slider("Spread", \.glowSpread, range: CameraRawSettings.toneRange, decimals: 0, clipping: nil,
                       help: "Sets how far the glow reaches. Has no effect until Glow is raised.")
                slider("Warmth", \.glowWarmth, range: CameraRawSettings.toneRange, decimals: 0, clipping: nil,
                       help: "Shifts the glow from cool to warm. Halation stays red. Has no effect until Glow is raised.")
            }
            .padding(.leading, 16)
            Text("晕影").font(.subheadline)
            slider("数量", \.vignetteAmount, range: CameraRawSettings.toneRange, decimals: 0, clipping: nil,
                   help: "Darkens or lightens the edges. The center does not change.")
            Picker("Style", selection: Binding(get: { raw.vignetteStyle }, set: { style in update { $0.cameraRaw.vignetteStyle = style } })) {
                ForEach(CameraRawVignetteStyle.allCases, id: \.self) { Text($0.rawValue).tag($0) }
            }
            .help("高光优先保护明亮边缘。颜色优先同时降低饱和度。叠加绘制则均匀覆盖边缘。")
            VStack(alignment: .leading, spacing: 8) {
                slider("Midpoint", \.vignetteMidpoint, range: CameraRawSettings.unitRange, decimals: 0, clipping: nil,
                       reset: 50, help: "Sets where the vignette begins, from the center outward.")
                slider("Roundness", \.vignetteRoundness, range: CameraRawSettings.toneRange, decimals: 0, clipping: nil,
                       help: "Makes the vignette rounder or more square.")
                slider("羽化", \.vignetteFeather, range: CameraRawSettings.unitRange, decimals: 0, clipping: nil,
                       reset: 50, help: "Softens the edge of the vignette.")
                slider("高光", \.vignetteHighlights, range: CameraRawSettings.unitRange, decimals: 0, clipping: nil,
                       help: "Protects bright pixels while a dark vignette is applied. Used by Highlight Priority.")
            }
            .padding(.leading, 16)
            Text("颗粒").font(.subheadline)
            slider("数量", \.grainAmount, range: CameraRawSettings.unitRange, decimals: 0, clipping: nil,
                   help: "Adds film grain, strongest in the middle tones.")
            slider("大小", \.grainSize, range: CameraRawSettings.unitRange, decimals: 0, clipping: nil,
                   reset: 25, help: "Makes the grain coarser or finer.")
            slider("Roughness", \.grainRoughness, range: CameraRawSettings.unitRange, decimals: 0, clipping: nil,
                   reset: 50, help: "Makes the grain smoother or more uneven.")
        }
    }

    private func eye(shown: Bool, name: String, group: PanelEye) -> some View {
        Button {
            switch group {
            case .light: session.filterEdit?.showsCameraRawLight.toggle()
            case .color: session.filterEdit?.showsCameraRawColor.toggle()
            case .effects: session.filterEdit?.showsCameraRawEffects.toggle()
            case .curve: session.filterEdit?.showsCameraRawCurve.toggle()
            case .mixer: session.filterEdit?.showsCameraRawMixer.toggle()
            case .grading: session.filterEdit?.showsCameraRawGrading.toggle()
            case .detail: session.filterEdit?.showsCameraRawDetail.toggle()
            case .optics: session.filterEdit?.showsCameraRawOptics.toggle()
            case .geometry: session.filterEdit?.showsCameraRawGeometry.toggle()
            case .calibration: session.filterEdit?.showsCameraRawCalibration.toggle()
            }
            if let edit = session.filterEdit { session.updateFilter(edit.settings, preview: edit.preview) }
        } label: {
            Image(systemName: shown ? "eye" : "eye.slash")
        }
        .buttonStyle(.borderless)
        .help(shown ? "Hide \(name) in the preview" : "Show \(name) in the preview")
        .accessibilityLabel(shown ? "Hide \(name)" : "Show \(name)")
    }

    private func slider(_ title: String, _ key: WritableKeyPath<CameraRawSettings, Double>, range: ClosedRange<Double>,
                        decimals: Int, clipping: CameraRawClipping?, track: CameraRawSliderTrack = .plain,
                        reset resetValue: Double = 0, help: String) -> some View {
        let step = pow(10, Double(decimals))
        return HStack(spacing: 10) {
            Text(title)
                .frame(minWidth: Self.labelWidth, alignment: .leading)
                .help(help)
                .onTapGesture(count: 2) { reset(key, to: resetValue) }
                .scrubbable(sensitivity: 1 / step,
                            value: Binding(get: { raw[keyPath: key] }, set: { assign(key, $0, clipping: nil) }),
                            range: range)
            CameraRawSlider(value: raw[keyPath: key], range: range, track: track, help: help,
                            onChange: { rawValue in assign(key, (rawValue * step).rounded() / step, clipping: clipping) },
                            onReset: { reset(key, to: resetValue) })
            TextField(title, value: Binding(get: { raw[keyPath: key] }, set: { assign(key, $0, clipping: nil) }),
                      format: .number.precision(.fractionLength(0...decimals)))
                .frame(width: 56).textFieldStyle(.roundedBorder).multilineTextAlignment(.trailing)
                .help(help)
        }
        .accessibilityElement(children: .contain)
        .accessibilityLabel(title)
    }

    private func setWhiteBalance(_ mode: CameraRawWhiteBalance) {
        if mode == .auto {
            Task { await session.applyCameraRawAutoWhiteBalance() }
            return
        }
        update { settings in
            settings.cameraRaw.whiteBalance = mode
        }
    }

    private func assign(_ key: WritableKeyPath<CameraRawSettings, Double>, _ newValue: Double, clipping: CameraRawClipping?) {
        let showClipping = clipping != nil && NSEvent.modifierFlags.contains(.option)
        session.filterEdit?.cameraRawClipping = showClipping ? clipping : nil
        update { settings in
            settings.cameraRaw[keyPath: key] = newValue
            if key == \.temperature || key == \.tint { settings.cameraRaw.whiteBalance = .custom }
        }
    }

    private func reset(_ key: WritableKeyPath<CameraRawSettings, Double>, to resetValue: Double) {
        session.filterEdit?.cameraRawClipping = nil
        assign(key, resetValue, clipping: nil)
    }

    private enum PanelEye { case light, color, effects, curve, mixer, grading, detail, optics, geometry, calibration }

    private func update(_ change: (inout FilterSettings) -> Void) {
        var value = settings
        change(&value)
        session.updateFilter(value, preview: session.filterEdit?.preview ?? true)
    }

    private func installOptionMonitor() {
        removeOptionMonitor()
        optionMonitor = NSEvent.addLocalMonitorForEvents(matching: .flagsChanged) { event in
            if !event.modifierFlags.contains(.option) {
                let edit = session.filterEdit
                if edit?.cameraRawClipping != nil || edit?.cameraRawSharpenMask == true {
                    edit?.cameraRawClipping = nil
                    edit?.cameraRawSharpenMask = false
                    if let edit { session.updateFilter(edit.settings, preview: edit.preview) }
                }
            }
            return event
        }
    }

    private func removeOptionMonitor() {
        if let optionMonitor { NSEvent.removeMonitor(optionMonitor) }
        optionMonitor = nil
    }

    static let labelWidth: CGFloat = 96

    private enum Section: String, CaseIterable, Identifiable {
        case light = "光线"
        case color = "颜色"
        case colorGrading = "颜色分级"
        case effects = "效果"
        case curve = "曲线"
        case colorMixer = "颜色混合器"
        case detail = "细节"
        case optics = "光学"
        case geometry = "几何"
        case calibration = "校准"
        var id: String { rawValue }
    }
}
