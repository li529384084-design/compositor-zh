import AppKit
import SwiftUI

// Compatibility shims: this build targets macOS 14, so the handful of macOS 15 conveniences the
// project uses are reimplemented here (or, where nothing equivalent exists, dropped).

// MARK: - onGeometryChange (macOS 15 and later)

/// Carries a geometry measurement up the view tree, the way `onGeometryChange` does.
private struct GeometryChangeKey<Value: Equatable>: PreferenceKey {
    static var defaultValue: Value? { nil }
    static func reduce(value: inout Value?, nextValue: () -> Value?) {
        if let next = nextValue() { value = next }
    }
}

extension View {
    /// `onGeometryChange(for:transform:action:)` for macOS 14: measure with a background
    /// `GeometryReader` and report the value through a preference.
    func onGeometryChangeCompat<Value: Equatable>(for type: Value.Type,
                                                  transform: @escaping (GeometryProxy) -> Value,
                                                  action: @escaping (Value) -> Void) -> some View {
        background(GeometryReader { proxy in
            Color.clear.preference(key: GeometryChangeKey<Value>.self, value: transform(proxy))
        })
        .onPreferenceChange(GeometryChangeKey<Value>.self) { value in
            if let value { action(value) }
        }
    }

    /// The offset a scroll view's content has been scrolled to, for macOS 14: the content's origin
    /// inside `space` is the negated offset, so it is measured in a named coordinate space.
    func scrollingOffsetCompat(in space: String, action: @escaping (CGPoint) -> Void) -> some View {
        background(GeometryReader { proxy in
            let origin = proxy.frame(in: .named(space)).origin
            Color.clear
                .onAppear { action(CGPoint(x: -origin.x, y: -origin.y)) }
                .onChange(of: origin) { _, new in action(CGPoint(x: -new.x, y: -new.y)) }
        })
    }

    /// `pointerStyle` for macOS 14, which has no cursor-style modifier: the cursor is set through
    /// AppKit while the pointer is over the view.
    func pointerStyleCompat(_ cursor: NSCursor) -> some View {
        onHover { inside in
            if inside { cursor.set() } else { NSCursor.arrow.set() }
        }
    }
}

// MARK: - Resize cursors (macOS 15 and later)

/// macOS 15 replaced the eight separate resize cursors with `NSCursor.frameResize(position:direction:)`, which draws
/// a double-headed arrow along whichever edge or corner was asked for. macOS 14 has only the four straight ones, so
/// the same arrow is made here by rotating the horizontal resize cursor; on the four straight directions the system's
/// own cursor is used unchanged.
enum FrameResizeDirection {
    case top, topRight, right, bottomRight, bottom, bottomLeft, left, topLeft

    /// Where the arrow points, in degrees clockwise, AppKit's y growing downwards.
    private var degrees: CGFloat {
        switch self {
        case .right: 0
        case .bottomRight: 45
        case .bottom: 90
        case .bottomLeft: 135
        case .left: 180
        case .topLeft: 225
        case .top: 270
        case .topRight: 315
        }
    }

    var cursor: NSCursor {
        switch degrees {
        case 0, 180: return .resizeLeftRight
        case 90, 270: return .resizeUpDown
        default: return Self.rotated[degrees, default: Self.rotated(.resizeLeftRight, byDegrees: degrees)]
        }
    }

    /// Rotated cursors are built once each: `cursorRect` runs on every mouse move.
    private static var rotated: [CGFloat: NSCursor] = [:]

    private static func rotated(_ cursor: NSCursor, byDegrees degrees: CGFloat) -> NSCursor {
        let source = cursor.image
        let size = source.size
        let image = NSImage(size: size)
        image.lockFocus()
        let transform = NSAffineTransform()
        transform.translateX(by: size.width / 2, yBy: size.height / 2)
        transform.rotate(byDegrees: degrees)
        transform.translateX(by: -size.width / 2, yBy: -size.height / 2)
        transform.concat()
        source.draw(at: .zero, from: NSRect(origin: .zero, size: size), operation: .sourceOver, fraction: 1)
        image.unlockFocus()
        return NSCursor(image: image, hotSpot: NSPoint(x: size.width / 2, y: size.height / 2))
    }
}
