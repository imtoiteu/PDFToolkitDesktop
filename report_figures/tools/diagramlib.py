"""
diagramlib — mô tả sơ đồ một lần, xuất ra hai định dạng:

  * <name>.drawio : XML mxGraph gốc (mọi hộp / mũi tên / nhãn đều là đối tượng
                    riêng, chỉnh sửa trực tiếp được trong diagrams.net)
  * <name>.svg    : SVG vector, dùng để chèn vào báo cáo Word

Hai bộ render dùng chung một mô hình toạ độ tuyệt đối và cùng một quy ước
điểm neo (exit/entry), nên hình trong Word và hình mở bằng draw.io khớp nhau.
"""

from __future__ import annotations

import html
import math
import os
import textwrap
import uuid

# --------------------------------------------------------------------------
# Bảng màu dùng chung cho toàn bộ hình vẽ của báo cáo
# --------------------------------------------------------------------------
PALETTE = {
    "ui":       ("#EEF2FF", "#4F46E5", "#1E1B4B"),   # tầng giao diện
    "logic":    ("#ECFDF5", "#059669", "#064E3B"),   # tầng nghiệp vụ / logic
    "engine":   ("#FFF7ED", "#EA580C", "#7C2D12"),   # thư viện xử lý / WASM
    "native":   ("#F1F5F9", "#334155", "#0F172A"),   # vỏ native / hệ điều hành
    "data":     ("#FEFCE8", "#CA8A04", "#713F12"),   # dữ liệu / tệp
    "external": ("#FDF2F8", "#DB2777", "#831843"),   # thành phần bên ngoài
    "neutral":  ("#FFFFFF", "#94A3B8", "#0F172A"),   # trung tính
    "accent":   ("#E0F2FE", "#0284C7", "#0C4A6E"),   # nhấn
    "warn":     ("#FEF2F2", "#DC2626", "#7F1D1D"),   # lỗi / cảnh báo
}

FONT = "Arial,Helvetica,sans-serif"


def _c(kind):
    return PALETTE.get(kind, PALETTE["neutral"])


# --------------------------------------------------------------------------
class Node:
    def __init__(self, nid, x, y, w, h, label, kind="neutral", shape="rect",
                 font_size=12, bold=False, dashed=False, sub=None, align="center"):
        self.id = nid
        self.x, self.y, self.w, self.h = x, y, w, h
        self.label = label
        self.kind = kind
        self.shape = shape           # rect | round | ellipse | actor | note | cyl | hex | diamond
        self.font_size = font_size
        self.bold = bold
        self.dashed = dashed
        self.sub = sub               # dòng phụ, chữ nhỏ hơn
        self.align = align

    # điểm neo theo phía
    def anchor(self, side):
        cx, cy = self.x + self.w / 2, self.y + self.h / 2
        return {
            "n": (cx, self.y),
            "s": (cx, self.y + self.h),
            "e": (self.x + self.w, cy),
            "w": (self.x, cy),
            "c": (cx, cy),
            "ne": (self.x + self.w, self.y),
            "nw": (self.x, self.y),
            "se": (self.x + self.w, self.y + self.h),
            "sw": (self.x, self.y + self.h),
        }[side]

    def rel(self, side):
        return {
            "n": (0.5, 0), "s": (0.5, 1), "e": (1, 0.5), "w": (0, 0.5),
            "c": (0.5, 0.5), "ne": (1, 0), "nw": (0, 0),
            "se": (1, 1), "sw": (0, 1),
        }[side]


class Group:
    """Khung bao (container) — chỉ để nhóm trực quan, không nối cạnh."""

    def __init__(self, gid, x, y, w, h, label, kind="neutral", font_size=12):
        self.id, self.x, self.y, self.w, self.h = gid, x, y, w, h
        self.label = label
        self.kind = kind
        self.font_size = font_size


class Edge:
    def __init__(self, src, dst, label="", exit="auto", entry="auto",
                 style="ortho", dashed=False, arrow="classic", font_size=10,
                 waypoints=None, label_dx=0, label_dy=-8, color=None,
                 start_arrow=False):
        self.src, self.dst = src, dst
        self.label = label
        self.exit, self.entry = exit, entry
        self.style = style           # ortho | straight
        self.dashed = dashed
        self.arrow = arrow           # classic | open | none
        self.font_size = font_size
        self.waypoints = waypoints or []
        self.label_dx, self.label_dy = label_dx, label_dy
        self.color = color or "#475569"
        self.start_arrow = start_arrow


class Scene:
    def __init__(self, title, width, height, bg="#FFFFFF"):
        self.title = title
        self.width, self.height = width, height
        self.bg = bg
        self.groups: list[Group] = []
        self.nodes: dict[str, Node] = {}
        self.order: list[str] = []
        self.edges: list[Edge] = []
        self.free_texts: list[tuple] = []   # (x, y, text, size, bold, anchor, color)
        self.k = 1.0                        # hệ số phóng theo chiều dọc

    # ---- builders -------------------------------------------------------
    def group(self, gid, x, y, w, h, label, kind="neutral", font_size=12):
        self.groups.append(Group(gid, x, y, w, h, label, kind, font_size))
        return gid

    def node(self, nid, x, y, w, h, label, **kw):
        n = Node(nid, x, y, w, h, label, **kw)
        self.nodes[nid] = n
        self.order.append(nid)
        return nid

    def edge(self, src, dst, label="", **kw):
        self.edges.append(Edge(src, dst, label, **kw))

    def text(self, x, y, s, size=11, bold=False, anchor="middle", color="#0F172A"):
        self.free_texts.append((x, y, s, size, bold, anchor, color))

    # ---- transform ------------------------------------------------------
    def vstretch(self, k):
        """Giãn hình theo chiều dọc và phóng to cỡ chữ cùng hệ số.

        Bề rộng giữ nguyên, nên khi hình được chèn vào trang giấy với bề
        rộng cố định, cỡ chữ thực tế trên bản in tăng theo đúng hệ số k.
        """
        if k <= 1.0:
            return self
        self.k = k
        self.height = int(self.height * k)
        for g in self.groups:
            g.y *= k
            g.h *= k
            g.font_size *= k
        for n in self.nodes.values():
            n.y *= k
            n.h *= k
            n.font_size *= k
            # Cỡ chữ lớn hơn trên cùng bề rộng hộp -> nhiều dòng hơn.
            # Nới chiều cao hộp vừa đủ chứa văn bản, có giới hạn trên để
            # không phá vỡ bố cục đã đặt.
            if n.label:
                fs = n.font_size
                ew = n.w * SHAPE_TEXT_RATIO.get(n.shape, 1.0)
                need = len(_wrap(n.label, ew, fs, n.bold)) * (fs + 3)
                if n.sub:
                    need += len(_wrap(n.sub, ew, fs - 2)) * (fs + 1) + 3
                need += 14 if n.shape not in SHAPE_TEXT_RATIO else 26
                cap = 1.5 if n.shape not in SHAPE_TEXT_RATIO else 1.9
                n.h = min(max(n.h, need), n.h * cap)
        for e in self.edges:
            e.font_size *= k
            e.waypoints = [(x, y * k) for (x, y) in e.waypoints]
        self.free_texts = [
            (x, y * k, t, sz * k, b, a, c)
            for (x, y, t, sz, b, a, c) in self.free_texts
        ]
        return self

    # ---- geometry helpers ----------------------------------------------
    def _auto_sides(self, a: Node, b: Node):
        acx, acy = a.x + a.w / 2, a.y + a.h / 2
        bcx, bcy = b.x + b.w / 2, b.y + b.h / 2
        dx, dy = bcx - acx, bcy - acy
        if abs(dx) > abs(dy) * 1.2:
            return ("e", "w") if dx > 0 else ("w", "e")
        return ("s", "n") if dy > 0 else ("n", "s")

    def _route(self, e: Edge):
        a, b = self.nodes[e.src], self.nodes[e.dst]
        ex, en = e.exit, e.entry
        if ex == "auto" or en == "auto":
            aex, aen = self._auto_sides(a, b)
            ex = aex if ex == "auto" else ex
            en = aen if en == "auto" else en
        p0 = a.anchor(ex)
        p1 = b.anchor(en)
        pts = [p0] + list(e.waypoints) + [p1]
        if e.style == "straight" or e.waypoints:
            return pts, ex, en
        # định tuyến vuông góc đơn giản, tôn trọng hướng thoát/vào
        x0, y0 = p0
        x1, y1 = p1
        if abs(x0 - x1) < 0.5 or abs(y0 - y1) < 0.5:
            return [p0, p1], ex, en
        if ex in ("n", "s") and en in ("n", "s"):
            my = (y0 + y1) / 2
            return [p0, (x0, my), (x1, my), p1], ex, en
        if ex in ("e", "w") and en in ("e", "w"):
            mx = (x0 + x1) / 2
            return [p0, (mx, y0), (mx, y1), p1], ex, en
        if ex in ("n", "s"):
            return [p0, (x0, y1), p1], ex, en
        return [p0, (x1, y0), p1], ex, en


# ==========================================================================
#  SVG renderer
# ==========================================================================
SHAPE_TEXT_RATIO = {
    "diamond": 0.62, "ellipse": 0.80, "hex": 0.84, "cyl": 0.92,
    "note": 0.90,
}


def _wrap(label, w, font_size, bold=False):
    """Ước lượng số ký tự mỗi dòng theo bề rộng hộp."""
    factor = 0.64 if bold else 0.60
    max_chars = max(6, int((w - 18) / (font_size * factor)))
    lines = []
    for para in label.split("\n"):
        if not para:
            lines.append("")
            continue
        lines.extend(textwrap.wrap(para, max_chars) or [""])
    return lines


def _poly_len(pts):
    return sum(math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1))


def _point_at(pts, frac):
    total = _poly_len(pts)
    if total == 0:
        return pts[0]
    target = total * frac
    acc = 0.0
    for i in range(len(pts) - 1):
        seg = math.dist(pts[i], pts[i + 1])
        if acc + seg >= target:
            t = (target - acc) / seg if seg else 0
            return (pts[i][0] + (pts[i + 1][0] - pts[i][0]) * t,
                    pts[i][1] + (pts[i + 1][1] - pts[i][1]) * t)
        acc += seg
    return pts[-1]


def render_svg(sc: Scene) -> str:
    E = html.escape
    K = sc.k
    SW = round(1.6 * min(K, 1.6), 2)      # bề dày nét vẽ
    MK = round(7 * min(K, 1.6), 1)        # cỡ đầu mũi tên
    out = []
    out.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'width="{sc.width}" height="{sc.height}" '
        f'viewBox="0 0 {sc.width} {sc.height}" '
        f'font-family="{FONT}">'
    )
    out.append("<defs>")
    for name, col in [("arw", "#475569"), ("arwd", "#DC2626"),
                      ("arwg", "#059669"), ("arwi", "#4F46E5"),
                      ("arwo", "#EA580C"), ("arwp", "#DB2777")]:
        out.append(
            f'<marker id="{name}" viewBox="0 0 10 10" refX="9" refY="5" '
            f'markerWidth="{MK}" markerHeight="{MK}" orient="auto-start-reverse">'
            f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{col}"/></marker>'
        )
    out.append(
        '<marker id="arwOpen" viewBox="0 0 10 10" refX="9" refY="5" '
        f'markerWidth="{MK}" markerHeight="{MK}" orient="auto-start-reverse">'
        '<path d="M 0 0 L 10 5 L 0 10" fill="none" stroke="#475569" '
        'stroke-width="1.4"/></marker>'
    )
    out.append("</defs>")
    out.append(f'<rect width="{sc.width}" height="{sc.height}" fill="{sc.bg}"/>')

    marker_by_color = {
        "#475569": "arw", "#DC2626": "arwd", "#059669": "arwg",
        "#4F46E5": "arwi", "#EA580C": "arwo", "#DB2777": "arwp",
    }

    # ---- containers ----
    for g in sc.groups:
        fill, stroke, txt = _c(g.kind)
        out.append(
            f'<rect x="{g.x}" y="{g.y}" width="{g.w}" height="{g.h}" rx="10" '
            f'fill="{fill}" fill-opacity="0.45" stroke="{stroke}" '
            f'stroke-width="1.4" stroke-dasharray="6 4"/>'
        )
        if g.label:
            out.append(
                f'<text x="{g.x + 12}" y="{g.y + g.font_size + 6}" '
                f'font-size="{g.font_size}" font-weight="700" fill="{txt}">'
                f"{E(g.label)}</text>"
            )

    # ---- edges ----
    for e in sc.edges:
        pts, ex, en = sc._route(e)
        d = "M " + " L ".join(f"{p[0]:.1f} {p[1]:.1f}" for p in pts)
        dash = ' stroke-dasharray="6 4"' if e.dashed else ""
        mk = marker_by_color.get(e.color, "arw")
        end_marker = "" if e.arrow == "none" else f' marker-end="url(#{mk})"'
        start_marker = f' marker-start="url(#{mk})"' if e.start_arrow else ""
        out.append(
            f'<path d="{d}" fill="none" stroke="{e.color}" stroke-width="1.6"'
            f'{dash}{end_marker}{start_marker}/>'
        )
        if e.label:
            lx, ly = _point_at(pts, 0.5)
            lx += e.label_dx
            ly += e.label_dy
            lines = e.label.split("\n")
            wlab = max(len(s) for s in lines) * e.font_size * 0.52 + 8
            hlab = len(lines) * (e.font_size + 2) + 4
            out.append(
                f'<rect x="{lx - wlab/2:.1f}" y="{ly - hlab + 4:.1f}" '
                f'width="{wlab:.1f}" height="{hlab:.1f}" rx="3" fill="#FFFFFF" '
                f'fill-opacity="0.92" stroke="none"/>'
            )
            for i, s in enumerate(lines):
                yy = ly - hlab + 4 + (i + 1) * (e.font_size + 2) - 2
                out.append(
                    f'<text x="{lx:.1f}" y="{yy:.1f}" font-size="{e.font_size}" '
                    f'text-anchor="middle" fill="#334155">{E(s)}</text>'
                )

    # ---- nodes ----
    for nid in sc.order:
        n = sc.nodes[nid]
        fill, stroke, txt = _c(n.kind)
        dash = ' stroke-dasharray="6 4"' if n.dashed else ""
        cx, cy = n.x + n.w / 2, n.y + n.h / 2

        if n.shape == "ellipse":
            out.append(
                f'<ellipse cx="{cx}" cy="{cy}" rx="{n.w/2}" ry="{n.h/2}" '
                f'fill="{fill}" stroke="{stroke}" stroke-width="{SW}"{dash}/>'
            )
        elif n.shape == "actor":
            a = K
            hx, hy = cx, n.y + 14 * a
            out.append(
                f'<circle cx="{hx}" cy="{hy}" r="{10*a:.1f}" fill="{fill}" '
                f'stroke="{stroke}" stroke-width="{SW}"/>'
                f'<path d="M {hx} {hy+10*a:.1f} L {hx} {hy+34*a:.1f} '
                f'M {hx-14*a:.1f} {hy+18*a:.1f} L {hx+14*a:.1f} {hy+18*a:.1f} '
                f'M {hx} {hy+34*a:.1f} L {hx-12*a:.1f} {hy+52*a:.1f} '
                f'M {hx} {hy+34*a:.1f} L {hx+12*a:.1f} {hy+52*a:.1f}" fill="none" '
                f'stroke="{stroke}" stroke-width="{SW*1.15:.2f}" stroke-linecap="round"/>'
            )
        elif n.shape == "note":
            f = 14 * K
            out.append(
                f'<path d="M {n.x} {n.y} H {n.x+n.w-f} L {n.x+n.w} {n.y+f} '
                f'V {n.y+n.h} H {n.x} Z" fill="{fill}" stroke="{stroke}" '
                f'stroke-width="1.4"{dash}/>'
                f'<path d="M {n.x+n.w-f} {n.y} V {n.y+f} H {n.x+n.w}" '
                f'fill="none" stroke="{stroke}" stroke-width="{SW}"/>'
            )
        elif n.shape == "cyl":
            ry = 10 * K
            out.append(
                f'<path d="M {n.x} {n.y+ry} A {n.w/2} {ry} 0 0 1 {n.x+n.w} {n.y+ry} '
                f'V {n.y+n.h-ry} A {n.w/2} {ry} 0 0 1 {n.x} {n.y+n.h-ry} Z" '
                f'fill="{fill}" stroke="{stroke}" stroke-width="{SW}"/>'
                f'<path d="M {n.x} {n.y+ry} A {n.w/2} {ry} 0 0 0 {n.x+n.w} {n.y+ry}" '
                f'fill="none" stroke="{stroke}" stroke-width="{SW}"/>'
            )
        elif n.shape == "diamond":
            out.append(
                f'<path d="M {cx} {n.y} L {n.x+n.w} {cy} L {cx} {n.y+n.h} '
                f'L {n.x} {cy} Z" fill="{fill}" stroke="{stroke}" '
                f'stroke-width="{SW}"{dash}/>'
            )
        elif n.shape == "hex":
            k = min(18, n.w / 5)
            out.append(
                f'<path d="M {n.x+k} {n.y} H {n.x+n.w-k} L {n.x+n.w} {cy} '
                f'L {n.x+n.w-k} {n.y+n.h} H {n.x+k} L {n.x} {cy} Z" '
                f'fill="{fill}" stroke="{stroke}" stroke-width="{SW}"{dash}/>'
            )
        else:  # rect / round
            rx = (8 if n.shape == "round" else 4) * K
            out.append(
                f'<rect x="{n.x}" y="{n.y}" width="{n.w}" height="{n.h}" rx="{rx}" '
                f'fill="{fill}" stroke="{stroke}" stroke-width="{SW}"{dash}/>'
            )

        # nhãn
        if n.shape == "actor":
            lines = _wrap(n.label, max(n.w, 90), n.font_size, n.bold)
            y0 = n.y + 82 * K
            for i, s in enumerate(lines):
                out.append(
                    f'<text x="{cx}" y="{y0 + i*(n.font_size+3)}" '
                    f'font-size="{n.font_size}" text-anchor="middle" '
                    f'font-weight="{"700" if n.bold else "400"}" fill="{txt}">'
                    f"{E(s)}</text>"
                )
            continue

        ew = n.w * SHAPE_TEXT_RATIO.get(n.shape, 1.0)
        lines = _wrap(n.label, ew, n.font_size, n.bold)
        sub_lines = _wrap(n.sub, ew, n.font_size - 2) if n.sub else []
        lh = n.font_size + 3
        slh = n.font_size + 1
        total = len(lines) * lh + (len(sub_lines) * slh + 3 if sub_lines else 0)
        y = cy - total / 2 + n.font_size
        tx = cx if n.align == "center" else n.x + 10
        anch = "middle" if n.align == "center" else "start"
        for s in lines:
            out.append(
                f'<text x="{tx}" y="{y:.1f}" font-size="{n.font_size}" '
                f'text-anchor="{anch}" font-weight="{"700" if n.bold else "400"}" '
                f'fill="{txt}">{E(s)}</text>'
            )
            y += lh
        if sub_lines:
            y += 2
            for s in sub_lines:
                out.append(
                    f'<text x="{tx}" y="{y:.1f}" font-size="{n.font_size-2}" '
                    f'text-anchor="{anch}" fill="{txt}" fill-opacity="0.75">'
                    f"{E(s)}</text>"
                )
                y += slh

    # ---- free text ----
    for (x, y, s, size, bold, anchor, color) in sc.free_texts:
        for i, line in enumerate(s.split("\n")):
            out.append(
                f'<text x="{x}" y="{y + i*(size+3)}" font-size="{size}" '
                f'text-anchor="{anchor}" font-weight="{"700" if bold else "400"}" '
                f'fill="{color}">{E(line)}</text>'
            )

    out.append("</svg>")
    return "\n".join(out)


# ==========================================================================
#  draw.io (mxGraph) renderer
# ==========================================================================
_SHAPE_STYLE = {
    "rect":    "rounded=0;whiteSpace=wrap;html=1;",
    "round":   "rounded=1;arcSize=12;whiteSpace=wrap;html=1;",
    "ellipse": "ellipse;whiteSpace=wrap;html=1;",
    "actor":   "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;",
    "note":    "shape=note;whiteSpace=wrap;html=1;size=14;",
    "cyl":     "shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=10;",
    "diamond": "rhombus;whiteSpace=wrap;html=1;",
    "hex":     "shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;",
}


def render_drawio(sc: Scene) -> str:
    def E(t):
        # html=1 nên xuống dòng phải là thẻ <br> (đã thoát trong thuộc tính XML)
        return html.escape(str(t)).replace("\n", "&lt;br&gt;")

    cells = []

    def esc_style(s):
        return s

    def R(v):
        return round(float(v), 1)

    for g in sc.groups:
        fill, stroke, txt = _c(g.kind)
        style = (
            f"rounded=1;arcSize=6;whiteSpace=wrap;html=1;dashed=1;dashPattern=6 4;"
            f"fillColor={fill};strokeColor={stroke};fontColor={txt};"
            f"verticalAlign=top;align=left;spacingLeft=10;spacingTop=4;"
            f"fontSize={R(g.font_size)};fontStyle=1;opacity=55;"
        )
        cells.append(
            f'<mxCell id="{g.id}" value="{E(g.label)}" style="{esc_style(style)}" '
            f'vertex="1" parent="1">'
            f'<mxGeometry x="{R(g.x)}" y="{R(g.y)}" width="{R(g.w)}" '
            f'height="{R(g.h)}" as="geometry"/></mxCell>'
        )

    for nid in sc.order:
        n = sc.nodes[nid]
        fill, stroke, txt = _c(n.kind)
        base = _SHAPE_STYLE.get(n.shape, _SHAPE_STYLE["rect"])
        if n.sub:
            value = (
                "&lt;b&gt;" + E(n.label) + "&lt;/b&gt;&lt;br&gt;"
                "&lt;font style=&#39;font-size:%dpx&#39;&gt;" % int(n.font_size - 2)
                + E(n.sub) + "&lt;/font&gt;"
            )
        else:
            value = E(n.label)
        style = (
            base
            + f"fillColor={fill};strokeColor={stroke};fontColor={txt};"
            + f"fontSize={R(n.font_size)};"
            + ("fontStyle=1;" if n.bold and not n.sub else "")
            + ("dashed=1;dashPattern=6 4;" if n.dashed else "")
            + ("align=left;spacingLeft=8;" if n.align != "center" else "")
        )
        if n.sub:
            style += "html=1;"
        cells.append(
            f'<mxCell id="{nid}" value="{value}" style="{esc_style(style)}" '
            f'vertex="1" parent="1">'
            f'<mxGeometry x="{n.x}" y="{n.y}" width="{n.w}" height="{n.h}" '
            f'as="geometry"/></mxCell>'
        )

    for i, e in enumerate(sc.edges):
        a, b = sc.nodes[e.src], sc.nodes[e.dst]
        ex, en = e.exit, e.entry
        if ex == "auto" or en == "auto":
            aex, aen = sc._auto_sides(a, b)
            ex = aex if ex == "auto" else ex
            en = aen if en == "auto" else en
        exx, exy = a.rel(ex)
        enx, eny = b.rel(en)
        estyle = (
            ("edgeStyle=orthogonalEdgeStyle;" if e.style == "ortho"
             else "edgeStyle=none;")
            + "rounded=0;html=1;jettySize=auto;orthogonalLoop=1;"
            + f"exitX={exx};exitY={exy};exitDx=0;exitDy=0;"
            + f"entryX={enx};entryY={eny};entryDx=0;entryDy=0;"
            + f"strokeColor={e.color};fontSize={R(e.font_size)};fontColor=#334155;"
            + ("dashed=1;dashPattern=6 4;" if e.dashed else "")
            + ("endArrow=none;" if e.arrow == "none" else
               "endArrow=open;endFill=0;" if e.arrow == "open" else
               "endArrow=classic;endFill=1;")
            + ("startArrow=classic;startFill=1;" if e.start_arrow else "")
            + "labelBackgroundColor=#FFFFFF;"
        )
        wps = ""
        if e.waypoints:
            pts = "".join(
                f'<mxPoint x="{R(p[0])}" y="{R(p[1])}" as="point"/>'
                for p in e.waypoints
            )
            wps = f'<Array as="points">{pts}</Array>'
        cells.append(
            f'<mxCell id="edge{i}" value="{E(e.label)}" style="{esc_style(estyle)}" '
            f'edge="1" parent="1" source="{e.src}" target="{e.dst}">'
            f'<mxGeometry relative="1" as="geometry">{wps}</mxGeometry></mxCell>'
        )

    for j, (x, y, s, size, bold, anchor, color) in enumerate(sc.free_texts):
        nlines = len(s.split("\n"))
        w = max(len(l) for l in s.split("\n")) * size * 0.6 + 10
        align = {"middle": "center", "start": "left", "end": "right"}[anchor]
        xx = x - w / 2 if anchor == "middle" else (x if anchor == "start" else x - w)
        style = (
            f"text;html=1;strokeColor=none;fillColor=none;align={align};"
            f"verticalAlign=middle;whiteSpace=wrap;fontSize={round(float(size),1)};"
            f"fontColor={color};" + ("fontStyle=1;" if bold else "")
        )
        cells.append(
            f'<mxCell id="txt{j}" value="{E(s)}" '
            f'style="{style}" vertex="1" parent="1">'
            f'<mxGeometry x="{xx:.0f}" y="{y - size:.0f}" width="{w:.0f}" '
            f'height="{nlines*(size+4)}" as="geometry"/></mxCell>'
        )

    body = "\n        ".join(cells)
    return (
        f'<mxfile host="app.diagrams.net" agent="PDFToolkitDesktop-report" '
        f'type="device">\n'
        f'  <diagram id="{uuid.uuid4().hex[:16]}" name="{E(sc.title)}">\n'
        f'    <mxGraphModel dx="{sc.width}" dy="{sc.height}" grid="1" gridSize="10" '
        f'guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" '
        f'pageScale="1" pageWidth="{sc.width}" pageHeight="{sc.height}" '
        f'math="0" shadow="0">\n'
        f"      <root>\n"
        f'        <mxCell id="0"/>\n'
        f'        <mxCell id="1" parent="0"/>\n'
        f"        {body}\n"
        f"      </root>\n"
        f"    </mxGraphModel>\n"
        f"  </diagram>\n"
        f"</mxfile>\n"
    )


# ==========================================================================
def auto_stretch(sc: Scene, target_ratio=1.375, kmax=2.0):
    """Chọn hệ số giãn dọc sao cho hình lấp đầy bề rộng trang in.

    target_ratio là tỉ lệ cao/rộng tối đa mà một hình còn được chèn với
    trọn bề rộng vùng chữ (16 cm) trên khổ A4 sau khi trừ chỗ cho chú
    thích hình.
    """
    ratio = sc.height / sc.width
    k = target_ratio / ratio
    k = max(1.0, min(kmax, k))
    return sc.vstretch(k)


def emit(sc: Scene, name, outdir, stretch=True):
    if stretch:
        auto_stretch(sc)
    svg_dir = os.path.join(outdir, "svg")
    dio_dir = os.path.join(outdir, "drawio")
    os.makedirs(svg_dir, exist_ok=True)
    os.makedirs(dio_dir, exist_ok=True)
    with open(os.path.join(svg_dir, name + ".svg"), "w", encoding="utf-8") as f:
        f.write(render_svg(sc))
    with open(os.path.join(dio_dir, name + ".drawio"), "w", encoding="utf-8") as f:
        f.write(render_drawio(sc))
    return name
