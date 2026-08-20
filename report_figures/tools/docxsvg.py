"""
Chèn ảnh SVG thật vào tài liệu Word.

Word 2016 trở lên hỗ trợ ảnh vector SVG thông qua phần mở rộng
`asvg:svgBlip` gắn vào phần tử <a:blip>, kèm một ảnh PNG dự phòng cho các
trình đọc cũ. Hàm add_svg_picture() dựng đúng cấu trúc đó: PNG được chèn
bằng python-docx như bình thường, sau đó phần tử blip được vá thêm tham
chiếu tới phần ảnh SVG.
"""

from __future__ import annotations

import io

import cairosvg
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.opc.packuri import PackURI
from docx.opc.part import Part
from docx.oxml.ns import qn
from docx.shared import Emu

SVG_EXT_URI = "{96DAC541-7B7A-43D3-8B79-37D633B846F1}"
ASVG_NS = "http://schemas.microsoft.com/office/drawing/2016/SVG/main"

_svg_counter = {"n": 0}


def _next_svg_partname(package):
    used = {p.partname for p in package.iter_parts()}
    while True:
        _svg_counter["n"] += 1
        name = PackURI("/word/media/vector%d.svg" % _svg_counter["n"])
        if name not in used:
            return name


def svg_size(svg_path):
    """Kích thước gốc của SVG tính theo pixel (đọc từ thuộc tính width/height)."""
    import re

    head = open(svg_path, "r", encoding="utf-8").read(2000)
    w = re.search(r'width="([\d.]+)"', head)
    h = re.search(r'height="([\d.]+)"', head)
    return float(w.group(1)), float(h.group(1))


def add_svg_picture(document, paragraph, svg_path, width, png_scale=2.0):
    """Chèn SVG vào `paragraph` với bề rộng `width` (docx.shared.Length).

    Ảnh PNG độ phân giải cao được nhúng làm bản dự phòng; ảnh SVG được
    nhúng làm bản hiển thị chính trong Word phiên bản mới.
    """
    w_px, h_px = svg_size(svg_path)
    height = Emu(int(width * h_px / w_px))

    png_bytes = cairosvg.svg2png(url=svg_path, scale=png_scale)
    run = paragraph.add_run()
    run.add_picture(io.BytesIO(png_bytes), width=width, height=height)

    # --- gắn phần ảnh SVG và vá <a:blip> -------------------------------
    doc_part = document.part
    svg_bytes = open(svg_path, "rb").read()
    partname = _next_svg_partname(doc_part.package)
    svg_part = Part(partname, "image/svg+xml", svg_bytes, doc_part.package)
    rId = doc_part.relate_to(svg_part, RT.IMAGE)

    blips = run._element.findall(".//" + qn("a:blip"))
    if not blips:
        return run
    blip = blips[-1]

    from docx.oxml import parse_xml

    ext_lst = parse_xml(
        '<a:extLst xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
        'xmlns:asvg="%s" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        '<a:ext uri="%s"><asvg:svgBlip r:embed="%s"/></a:ext>'
        "</a:extLst>" % (ASVG_NS, SVG_EXT_URI, rId)
    )
    blip.append(ext_lst)
    return run
