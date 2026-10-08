import SwiftUI

@MainActor
struct JPEGExportSheet: View {
    let raster: ExportRaster
    let session: EditorSession
    let finish: (Data?) -> Void
    @State private var options: JPEGOptions
    /// The quality of the last export, which the next one starts from.
    private static let qualityKey = "jpegExportQuality"

    init(raster: ExportRaster, session: EditorSession, finish: @escaping (Data?) -> Void) {
        self.raster = raster
        self.session = session
        self.finish = finish
        var start = JPEGOptions()
        if let saved = UserDefaults.standard.object(forKey: Self.qualityKey) as? Double, saved.isFinite {
            start.quality = min(1, max(0, saved))
        }
        _options = State(initialValue: start)
    }
    @State private var result: JPEGResult?
    /// The preview's zoom, 1 being 100%; nil fits the whole image.
    @State private var zoom: Double?
    @Environment(\.displayScale) private var displayScale
    /// The zoom shown now, Fit's included.
    private var shownZoom: Double {
        zoom ?? JPEGPreview.fitZoom(width: raster.image.width, height: raster.image.height,
                                    in: JPEGPreview.frame, displayScale: displayScale)
    }
    @State private var readyOptions: JPEGOptions?
    @State private var error: String?

    var body: some View { sheet.roundedControls() }
    @ViewBuilder private var sheet: some View {
        VStack(alignment: .leading, spacing: 16) {
            HStack(spacing: 8) {
                Text("导出 JPEG").font(.title2.bold())
                Spacer()
                Button("适合窗口") { zoom = nil }.disabled(zoom == nil)
                    .help("显示整幅图像 (⌘0)")
                Button { zoomBy(1) } label: { Image(systemName: "plus.magnifyingglass") }
                    .disabled(JPEGPreview.step(from: shownZoom, in: 1) == nil)
                    .help("放大 (⌘+)，当前 \(percent)。100% 时 JPEG 的每个像素对应屏幕的一个像素，与画布一致")
                Button { zoomBy(-1) } label: { Image(systemName: "minus.magnifyingglass") }
                    .disabled(JPEGPreview.step(from: shownZoom, in: -1) == nil)
                    .help("缩小 (⌘−)，当前 \(percent)")
            }
            // Closer to the title row than the rest of the dialog's spacing.
            .padding(.bottom, -8)
            ZStack {
                Color(white: 0.12)
                if let result {
                    JPEGPreview(image: result.preview, pixelWidth: raster.image.width, pixelHeight: raster.image.height, zoom: $zoom)
                }
                if readyOptions != options && error == nil {
                    ProgressView().padding().background(.regularMaterial, in: RoundedRectangle(cornerRadius: 8))
                }
            }.frame(width: JPEGPreview.frame.width, height: JPEGPreview.frame.height).clipped()
                .help("拖动或滚动可平移视图；双击可在适合窗口与 100% 之间切换")
            HStack {
                Text("品质")
                Slider(value: $options.quality, in: 0...1, step: 0.01)
                Text("\(Int((options.quality * 100).rounded()))%")
                    .monospacedDigit().frame(width: 45, alignment: .trailing)
            }
            HStack(spacing: 8) {
                Text("透明区域背景")
                DialogColorSwatch(title: "JPEG Background", color: matte, session: session)
                    .help("用于填充透明区域的颜色")
            }
            HStack(spacing: 12) {
                Text("\(raster.image.width.formatted()) × \(raster.image.height.formatted()) px · sRGB")
                    .foregroundStyle(.secondary)
                Spacer()
                if let error { Text(error).foregroundStyle(.red) }
                else if readyOptions == options, let result {
                    Text(ByteCountFormatter.string(fromByteCount: Int64(result.data.count), countStyle: .file)).monospacedDigit()
                } else { Text("正在更新…").foregroundStyle(.secondary) }
                Button("取消") { DialogColorSwatch.closePicker(session); finish(nil) }.configuredNativeShortcut(.escape)
                Button("导出…") {
                    DialogColorSwatch.closePicker(session)
                    UserDefaults.standard.set(options.quality, forKey: Self.qualityKey)
                    finish(result?.data)
                }
                    .configuredNativeShortcut(.return)
                    .disabled(result == nil || readyOptions != options || error != nil)
            }
        }
        .padding(24)
        .onAppear { session.previewZoom = { command in
            switch command {
            case .zoomIn: zoomBy(1)
            case .zoomOut: zoomBy(-1)
            case .fit: zoom = nil
            case .actual: zoom = 1
            }
        } }
        .onDisappear { session.previewZoom = nil }
        .task(id: options) {
            let requested = options
            error = nil
            do {
                try await Task.sleep(for: .milliseconds(200))
                let encoded = try await ImageExporter.shared.jpeg(raster, options: requested)
                try Task.checkCancellation()
                result = encoded
                readyOptions = requested
            } catch is CancellationError {
                // A newer setting superseded this preview.
            } catch {
                guard !Task.isCancelled else { return }
                self.error = error.localizedDescription
            }
        }
    }

    private var percent: String { "\(Int((shownZoom * 100).rounded()))%" }
    private func zoomBy(_ direction: Int) {
        if let next = JPEGPreview.step(from: shownZoom, in: direction) { zoom = next }
    }
    private var matte: Binding<PaletteColor> {
        Binding(get: { PaletteColor(red: options.red, green: options.green, blue: options.blue) },
                set: { options.red = $0.red; options.green = $0.green; options.blue = $0.blue })
    }
}

/// The encoded JPEG, fitted or zoomed (1 is 100%: one image pixel per screen pixel, as the canvas counts it), where it
/// can be dragged or scrolled around. Double-click switches between Fit and 100%.
@MainActor
struct JPEGPreview: View {
    static let frame = CGSize(width: 560, height: 330)
    static let steps: [Double] = [0.25, 0.5, 1, 2, 4, 8]
    /// The scroll view is steered by moving this 1-point marker and asking `ScrollViewReader` to bring it to the
    /// view's top-left corner: `ScrollPosition` and `scrollTo(point:)`, which did this in one call, are macOS 15.
    private static let markerID = "jpegPreviewMarker"
    let image: CGImage
    /// The exported image's size, which the preview may have been decoded smaller than.
    let pixelWidth: Int
    let pixelHeight: Int
    @Binding var zoom: Double?
    @Environment(\.displayScale) private var displayScale
    /// Where the marker sits in the image, which is the offset the scroll view is showing it at.
    @State private var marker = CGPoint.zero
    @State private var offset = CGPoint.zero
    @State private var dragStart: CGPoint?

    /// The zoom at which the whole image fits `frame`.
    static func fitZoom(width: Int, height: Int, in frame: CGSize, displayScale: CGFloat) -> Double {
        let points = CGSize(width: CGFloat(width) / max(1, displayScale), height: CGFloat(height) / max(1, displayScale))
        return Double(min(frame.width / points.width, frame.height / points.height))
    }
    /// The next zoom step past `zoom` in `direction` (1 in, −1 out), or nil at the end.
    static func step(from zoom: Double, in direction: Int) -> Double? {
        direction > 0 ? steps.first { $0 > zoom * 1.001 } : steps.last { $0 < zoom * 0.999 }
    }

    var body: some View {
        GeometryReader { geometry in
            if let zoom {
                let size = shownSize(zoom)
                ScrollViewReader { proxy in
                    ScrollView([.horizontal, .vertical]) {
                        ZStack(alignment: .topLeading) {
                            // Nearest-neighbor from 100% up, so each pixel of the JPEG and its artifacts shows as it is.
                            Image(decorative: image, scale: 1).resizable().interpolation(zoom >= 1 ? .none : .high)
                                .frame(width: size.width, height: size.height)
                            // `id` before `padding`: padding places the marker at the offset while the scroll view
                            // still aligns on the marker itself.
                            Color.clear.frame(width: 1, height: 1)
                                .id(Self.markerID)
                                .padding(.leading, marker.x)
                                .padding(.top, marker.y)
                        }
                        .frame(minWidth: geometry.size.width, minHeight: geometry.size.height)
                        .scrollingOffsetCompat(in: "jpegPreview") {
                            offset = CGPoint(x: max(0, $0.x), y: max(0, $0.y))
                        }
                    }
                    .scrollIndicators(.visible)
                    .coordinateSpace(name: "jpegPreview")
                    .gesture(DragGesture(minimumDistance: 1)
                        .onChanged { drag in
                            let start = dragStart ?? offset
                            dragStart = start
                            scroll(to: CGPoint(x: start.x - drag.translation.width, y: start.y - drag.translation.height),
                                   content: size, viewport: geometry.size, proxy: proxy)
                        }
                        .onEnded { _ in dragStart = nil })
                    .onTapGesture(count: 2) { self.zoom = nil }
                    .onAppear { keepCentered(from: nil, to: zoom, content: size, viewport: geometry.size, proxy: proxy) }
                    .onChange(of: zoom) { old, new in
                        // `zoom` is shadowed by the unwrapped value here, so `new` is a plain Double.
                        keepCentered(from: old, to: new, content: shownSize(new), viewport: geometry.size, proxy: proxy)
                    }
                    .pointerStyleCompat(dragStart == nil ? .openHand : .closedHand)
                }
            } else {
                Image(decorative: image, scale: 1).resizable().interpolation(.high).scaledToFit()
                    .frame(width: geometry.size.width, height: geometry.size.height)
                    .contentShape(Rectangle())
                    .onTapGesture(count: 2) { self.zoom = 1 }
            }
        }
    }

    /// The image's size on screen at `zoom`, in points.
    private func shownSize(_ zoom: Double) -> CGSize {
        CGSize(width: CGFloat(pixelWidth) / max(1, displayScale) * zoom, height: CGFloat(pixelHeight) / max(1, displayScale) * zoom)
    }

    /// Zooming keeps the middle of the view on the same part of the image; coming from Fit, it starts at the center.
    private func keepCentered(from old: Double?, to new: Double?, content size: CGSize, viewport: CGSize,
                              proxy: ScrollViewProxy) {
        guard new != nil else { return }
        var middle = CGPoint(x: size.width / 2, y: size.height / 2)
        if let old {
            let before = shownSize(old)
            let fx = before.width > 0 ? (offset.x + min(viewport.width, before.width) / 2) / before.width : 0.5
            let fy = before.height > 0 ? (offset.y + min(viewport.height, before.height) / 2) / before.height : 0.5
            middle = CGPoint(x: fx * size.width, y: fy * size.height)
        }
        scroll(to: CGPoint(x: middle.x - viewport.width / 2, y: middle.y - viewport.height / 2),
               content: size, viewport: viewport, proxy: proxy)
    }

    /// Puts `point` of the image at the preview's top-left corner, within the range it can scroll.
    private func scroll(to point: CGPoint, content size: CGSize, viewport: CGSize, proxy: ScrollViewProxy) {
        let clamped = CGPoint(x: min(max(0, point.x), max(0, size.width - viewport.width)),
                              y: min(max(0, point.y), max(0, size.height - viewport.height)))
        marker = clamped
        // After the marker has been laid out at its new place, not during the same update.
        DispatchQueue.main.async { proxy.scrollTo(Self.markerID, anchor: .topLeading) }
    }
}
