# report_figures — hình vẽ và tài liệu kèm theo báo cáo

Thư mục này chứa toàn bộ hình vẽ kỹ thuật của báo cáo
`BAO_CAO_DE_TAI_PDFTOOLKIT_DESKTOP.docx`, cùng công cụ để tái sinh chúng.

## Cấu trúc

```
report_figures/
├── drawio/               bản gốc mxGraph, chỉnh sửa được (nguồn chuẩn)
├── svg/                  bản vector, được chèn vào tệp Word (nguồn chuẩn)
├── png/                  bản raster để xem nhanh, không dùng trong báo cáo
├── chapter2/             bản sao .drawio + .svg của các hình chương 2
├── chapter3/             bản sao .drawio + .svg của các hình chương 3
├── chapter4/             bản sao .drawio + .svg của các hình chương 4
├── screenshots/          nơi đặt ảnh chụp giao diện bổ sung thủ công
├── tools/                mã nguồn sinh hình và sinh báo cáo
├── FIGURE_INDEX.md       chỉ mục hình kèm bằng chứng mã nguồn và trạng thái
├── MANUAL_SCREENSHOTS.md hướng dẫn chụp 11 ảnh giao diện còn thiếu
└── README.md             tệp này
```

Các thư mục `chapter2/`, `chapter3/`, `chapter4/` chỉ là bản sao gom nhóm theo
chương cho tiện tra cứu. Nguồn chuẩn là `drawio/` và `svg/`; khi sửa hình, hãy
sửa mã trong `tools/` rồi chạy lại các kịch bản bên dưới.

## Tái sinh toàn bộ

```bash
cd tools
python3 fig_ch2.py      # Hình 2.1 – 2.13
python3 fig_ch3.py      # Hình 3.1 – 3.13 (phần sơ đồ)
python3 fig_ch4.py      # Hình 4.1 – 4.5
python3 make_report.py  # dựng lại BAO_CAO_DE_TAI_PDFTOOLKIT_DESKTOP.docx
python3 make_index.py   # dựng lại FIGURE_INDEX.md và MANUAL_SCREENSHOTS.md
```

Yêu cầu: Python 3 với `python-docx` và `cairosvg`.

## Ghi chú kỹ thuật

* `tools/diagramlib.py` — mô tả sơ đồ một lần, xuất ra đồng thời `.drawio` và
  `.svg` với cùng một hệ toạ độ và cùng quy ước điểm neo, nên hình trong Word
  và hình mở bằng diagrams.net khớp nhau.
* `tools/docxsvg.py` — nhúng SVG thật vào Word bằng phần mở rộng
  `asvg:svgBlip`, kèm ảnh PNG độ phân giải cao làm bản dự phòng.
* `tools/builder.py` — dựng tài liệu Word theo đúng định dạng của bộ báo cáo:
  khổ A4, lề 3,5 / 1,5 / 2,5 / 2 cm, Times New Roman 14 pt, giãn dòng 1,2,
  thụt dòng đầu 1,25 cm.
