#!/usr/bin/env python3
"""Dựng tệp báo cáo Word hoàn chỉnh cho đề tài PDF Toolkit Desktop."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from builder import Report  # noqa: E402
import content_a  # noqa: E402
import content_b  # noqa: E402
import content_c  # noqa: E402
import content_d  # noqa: E402

OUT = "/root/imtoiteu/PDFToolKit/BAO_CAO_DE_TAI_PDFTOOLKIT_DESKTOP.docx"


def main():
    r = Report()
    r.page_numbers()
    content_a.build(r)
    content_b.build(r)
    content_c.build(r)
    content_d.build(r)
    r.save(OUT)

    doc = r.doc
    words = sum(len(p.text.split()) for p in doc.paragraphs)
    twords = sum(
        len(c.text.split())
        for t in doc.tables for row in t.rows for c in row.cells
    )
    print("Đã lưu:", OUT)
    print("Số đoạn:", len(doc.paragraphs))
    print("Số bảng:", len(doc.tables))
    print("Số từ trong đoạn văn:", words)
    print("Số từ trong bảng:", twords)
    print("Số hình vector đã chèn:", len(r.used_figs))
    print("Số khung giữ chỗ ảnh chụp:", len(r.placeholders))
    heads = [p for p in doc.paragraphs if p.style.name.startswith("Heading")]
    print("Số tiêu đề:", len(heads))
    return r


if __name__ == "__main__":
    main()
