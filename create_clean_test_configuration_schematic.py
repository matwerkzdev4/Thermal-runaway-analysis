from __future__ import annotations

from html import escape
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "report_figures"
PNG_OUT = OUT_DIR / "Thermal_Runaway_Test_Configuration_Clean.png"
SVG_OUT = OUT_DIR / "Thermal_Runaway_Test_Configuration_Clean.svg"

W, H = 1920, 1080
BG = "#f7f9fc"
INK = "#18202a"
MUTED = "#566270"
BLUE = "#4f95d8"
BLUE_EDGE = "#1f5d93"
RED = "#e33a3a"
BLACK = "#111111"
YELLOW = "#ffd84d"
ORANGE = "#e87524"
LIGHT = "#ffffff"
GRID = "#d7dee8"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
        Path("C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default(size=size)


F_TITLE = font(48, True)
F_CELL = font(42, True)
F_LABEL = font(25, True)
F_BODY = font(25)
F_SMALL = font(22)
F_LEGEND = font(21)
F_LEGEND_BOLD = font(21, True)
F_NOTE = font(19)


CELL_Y0 = 220
CELL_H = 500
CELL_W = 220
CELL_XS = [250, 570, 890, 1198, 1506]
JACKET_W = 14
HEATER_W = 12
TC_R = 10
SURFACE_GAP = TC_R * 2
HEATER_JACKET_GAP = HEATER_W + TC_R * 2

CELLS = {
    f"C{i + 1}": (
        CELL_XS[i],
        CELL_Y0,
        CELL_XS[i] + CELL_W,
        CELL_Y0 + CELL_H,
    )
    for i in range(5)
}


def jacket_gap(cell: str) -> int:
    return HEATER_JACKET_GAP if cell == "C2" else SURFACE_GAP

def left_jacket(cell: str):
    x0, y0, _, y1 = CELLS[cell]
    gap = jacket_gap(cell)
    return (x0 - gap - JACKET_W, y0 - 25, x0 - gap, y1 + 25)


def right_jacket(cell: str):
    _, y0, x1, y1 = CELLS[cell]
    gap = jacket_gap(cell)
    return (x1 + gap, y0 - 25, x1 + gap + JACKET_W, y1 + 25)


JACKETS = [
    left_jacket("C1"),
    right_jacket("C1"),
    left_jacket("C2"),
    right_jacket("C2"),
    left_jacket("C3"),
    right_jacket("C3"),
    left_jacket("C4"),
    right_jacket("C4"),
    left_jacket("C5"),
    right_jacket("C5"),
]

c2_x0, c2_y0, c2_x1, c2_y1 = CELLS["C2"]
HEATERS = [
    (c2_x0 - HEATER_W, c2_y0, c2_x0, c2_y1),
    (c2_x1, c2_y0, c2_x1 + HEATER_W, c2_y1),
]


def center_x(cell: str) -> int:
    x0, _, x1, _ = CELLS[cell]
    return (x0 + x1) // 2


def mid_between(cell_a: str, cell_b: str) -> int:
    return (right_jacket(cell_a)[2] + left_jacket(cell_b)[0]) // 2


def left_surface_gap(cell: str) -> int:
    return (left_jacket(cell)[2] + CELLS[cell][0]) // 2


def right_surface_gap(cell: str) -> int:
    return (CELLS[cell][2] + right_jacket(cell)[0]) // 2


TC_POINTS = {
    "T1": (left_jacket("C1")[0], CELL_Y0 + 205),
    "T2": (left_surface_gap("C1"), CELL_Y0 + 325),
    "T3": (center_x("C1"), CELL_Y0),
    "T4": (right_surface_gap("C1"), CELL_Y0 + 250),
    "T5": (mid_between("C1", "C2"), CELL_Y0 + 380),
    "T6": ((left_jacket("C2")[2] + HEATERS[0][0]) // 2, CELL_Y0 + 270),
    "T7": (center_x("C2"), CELL_Y0),
    "T8": ((HEATERS[1][2] + right_jacket("C2")[0]) // 2, CELL_Y0 + 270),
    "T9": (mid_between("C2", "C3"), CELL_Y0 + 380),
    "T10": (left_surface_gap("C3"), CELL_Y0 + 250),
    "T11": (center_x("C3"), CELL_Y0),
    "T12": (right_surface_gap("C3"), CELL_Y0 + 250),
    "T13": (mid_between("C3", "C4"), CELL_Y0 + 380),
    "T14": (left_surface_gap("C4"), CELL_Y0 + 250),
    "T15": (center_x("C4"), CELL_Y0),
    "T16": (right_surface_gap("C4"), CELL_Y0 + 250),
    "T17": (mid_between("C4", "C5"), CELL_Y0 + 380),
    "T18": (left_surface_gap("C5"), CELL_Y0 + 250),
    "T19": (center_x("C5"), CELL_Y0),
    "T20": (right_surface_gap("C5"), CELL_Y0 + 250),
    "T21": (right_jacket("C5")[2], CELL_Y0 + 380),
}

LABEL_POS = {
    "T1": (92, CELL_Y0 + 170),
    "T2": (96, CELL_Y0 + 358),
    "T3": (center_x("C1") - 22, CELL_Y0 - 66),
    "T4": (CELLS["C1"][2] - 58, CELL_Y0 + 210),
    "T5": (mid_between("C1", "C2") - 46, CELL_Y0 + 452),
    "T6": (HEATERS[0][0] - 84, CELL_Y0 + 205),
    "T7": (center_x("C2") - 22, CELL_Y0 - 66),
    "T8": (HEATERS[1][2] - 80, CELL_Y0 + 140),
    "T9": (mid_between("C2", "C3") - 42, CELL_Y0 + 452),
    "T10": (CELLS["C3"][0] + 12, CELL_Y0 + 145),
    "T11": (center_x("C3") - 30, CELL_Y0 - 66),
    "T12": (CELLS["C3"][2] - 72, CELL_Y0 + 210),
    "T13": (mid_between("C3", "C4") - 48, CELL_Y0 + 452),
    "T14": (CELLS["C4"][0] - 74, CELL_Y0 + 145),
    "T15": (center_x("C4") - 30, CELL_Y0 - 66),
    "T16": (CELLS["C4"][2] - 72, CELL_Y0 + 210),
    "T17": (mid_between("C4", "C5") - 48, CELL_Y0 + 452),
    "T18": (CELLS["C5"][0] - 66, CELL_Y0 + 145),
    "T19": (center_x("C5") - 30, CELL_Y0 - 66),
    "T20": (CELLS["C5"][2] - 72, CELL_Y0 + 210),
    "T21": (right_jacket("C5")[0] - 78, CELL_Y0 + 452),
}


class Svg:
    def __init__(self) -> None:
        self.items: list[str] = []

    def rect(self, x0, y0, x1, y1, fill, stroke=None, sw=1, rx=0):
        stroke_attr = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        self.items.append(
            f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="{rx}" fill="{fill}"{stroke_attr}/>'
        )

    def line(self, x0, y0, x1, y1, stroke, sw=2):
        self.items.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="{stroke}" stroke-width="{sw}"/>')

    def circle(self, x, y, r, fill, stroke=INK, sw=3):
        self.items.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def text(self, x, y, text, size=24, weight="400", fill=INK, anchor="start"):
        self.items.append(
            f'<text x="{x}" y="{y}" font-family="Arial, Segoe UI, sans-serif" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{escape(text)}</text>'
        )

    def save(self, path: Path):
        content = "\n".join(self.items)
        path.write_text(
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n{content}\n</svg>\n',
            encoding="utf-8",
        )


def rounded(draw: ImageDraw.ImageDraw, box, fill, outline=None, width=1, radius=8):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def centered_text(draw: ImageDraw.ImageDraw, xy, text: str, fnt, fill):
    bbox = draw.textbbox((0, 0), text, font=fnt)
    draw.text((xy[0] - (bbox[2] - bbox[0]) / 2, xy[1] - (bbox[3] - bbox[1]) / 2), text, font=fnt, fill=fill)


def draw_label_png(draw: ImageDraw.ImageDraw, x: int, y: int, text: str):
    pad_x = 6
    pad_y = 3
    bbox = draw.textbbox((x, y), text, font=F_LABEL)
    box = (bbox[0] - pad_x, bbox[1] - pad_y, bbox[2] + pad_x, bbox[3] + pad_y)
    draw.rounded_rectangle(box, radius=4, fill="#f7f9fc", outline="#cfd8e4", width=1)
    draw.text((x, y), text, font=F_LABEL, fill=INK)


SURFACE_TCS = {"T2", "T4", "T10", "T12", "T14", "T16", "T18", "T20"}
HEATER_JACKET_TCS = {"T6", "T8"}


def tc_radius(tc: str) -> int:
    return TC_R


def svg_label(svg: Svg, x: int, y: int, text: str):
    width = 34 if len(text) == 2 else 48
    svg.rect(x - 6, y - 20, x + width, y + 9, "#f7f9fc", "#cfd8e4", 1, 4)
    svg.text(x, y + 4, text, 25, "700")


def draw_common_png(draw: ImageDraw.ImageDraw):
    draw.rectangle((0, 0, W, H), fill=BG)
    draw.text((54, 54), "Thermal Runaway Test Configuration", font=F_TITLE, fill=INK)

    # Subtle setup area.
    draw.rounded_rectangle((45, 145, 1875, 785), radius=12, fill="#eef3f8", outline=GRID, width=2)

    for box in JACKETS:
        draw.rectangle(box, fill=BLACK)
    for box in HEATERS:
        draw.rectangle(box, fill=RED)

    for cell, box in CELLS.items():
        rounded(draw, box, BLUE, BLUE_EDGE, width=3, radius=6)
        x0, y0, x1, y1 = box
        centered_text(draw, ((x0 + x1) / 2, (y0 + y1) / 2), cell, F_CELL, LIGHT)

    for tc, (x, y) in TC_POINTS.items():
        lx, ly = LABEL_POS[tc]
        draw.line((lx + 28, ly + 10, x, y), fill=ORANGE, width=3)
        r = tc_radius(tc)
        draw.ellipse((x - r, y - r, x + r, y + r), fill=YELLOW, outline=INK, width=3)
        draw_label_png(draw, lx, ly, tc)

    # Legend band.
    draw.rounded_rectangle((45, 795, 1875, 1065), radius=10, fill=LIGHT, outline=GRID, width=2)
    draw.text((75, 835), "Legend", font=F_LABEL, fill=INK)

    x = 75
    y = 890
    swatches = [
        (BLUE, "CATL 117 Ah battery cells", "square"),
        (RED, "Heater", "square"),
        (BLACK, "Insulation jacket", "square"),
        (YELLOW, "Thermocouple", "circle"),
    ]
    for color, label, shape in swatches:
        if shape == "circle":
            draw.ellipse((x, y - 16, x + 28, y + 12), fill=color, outline=INK, width=2)
        else:
            draw.rectangle((x, y - 16, x + 28, y + 12), fill=color, outline=INK if color != BLACK else BLACK, width=2)
        draw.text((x + 42, y - 18), label, font=F_LEGEND, fill=INK)
        x += 360

    col1_x, col2_x, col3_x = 75, 675, 1280
    col_y = 940
    draw.text((col1_x, col_y), "Cell / test notes", font=F_LEGEND_BOLD, fill=INK)
    draw.text((col1_x, col_y + 32), "- C2 = trigger cell", font=F_LEGEND, fill=INK)
    draw.text((col1_x, col_y + 60), "- Heaters turned off after C2 entered TR", font=F_LEGEND, fill=INK)
    draw.text((col1_x + 24, col_y + 86), "  assumed ~3 s after steepest T7 spike", font=F_NOTE, fill=INK)

    draw.text((col2_x, col_y), "Thermocouple information", font=F_LEGEND_BOLD, fill=INK)
    draw.text((col2_x, col_y + 32), "- Vent area: T3 / T7 / T11 / T15 / T19", font=F_LEGEND, fill=INK)
    draw.text((col2_x, col_y + 60), "- Battery surface:", font=F_LEGEND, fill=INK)
    draw.text((col2_x + 24, col_y + 86), "  T2 / T4 / T10 / T12 / T14 / T16 / T18 / T20", font=F_NOTE, fill=INK)

    draw.text((col3_x, col_y), "Thermocouple information", font=F_LEGEND_BOLD, fill=INK)
    draw.text((col3_x, col_y + 32), "- Inter-jacket: T5 / T9 / T13 / T17", font=F_LEGEND, fill=INK)
    draw.text((col3_x, col_y + 60), "- Heater/jacket: T6 / T8", font=F_LEGEND, fill=INK)
    draw.text((col3_x, col_y + 88), "- Outer jacket/air: T1 / T21", font=F_LEGEND, fill=INK)


def draw_svg(svg: Svg):
    svg.rect(0, 0, W, H, BG)
    svg.text(54, 92, "Thermal Runaway Test Configuration", 48, "700")
    svg.rect(45, 145, 1875, 785, "#eef3f8", GRID, 2, 12)

    for box in JACKETS:
        svg.rect(*box, BLACK)
    for box in HEATERS:
        svg.rect(*box, RED)
    for cell, (x0, y0, x1, y1) in CELLS.items():
        svg.rect(x0, y0, x1, y1, BLUE, BLUE_EDGE, 3, 6)
        svg.text((x0 + x1) / 2, (y0 + y1) / 2 + 16, cell, 42, "700", LIGHT, "middle")

    for tc, (x, y) in TC_POINTS.items():
        lx, ly = LABEL_POS[tc]
        svg.line(lx + 28, ly + 10, x, y, ORANGE, 3)
        svg.circle(x, y, tc_radius(tc), YELLOW, INK, 3)
        svg_label(svg, lx, ly + 21, tc)

    svg.rect(45, 795, 1875, 1065, LIGHT, GRID, 2, 10)
    svg.text(75, 860, "Legend", 25, "700")

    x = 75
    y = 890
    for color, label, shape in [
        (BLUE, "CATL 117 Ah battery cells", "square"),
        (RED, "Heater", "square"),
        (BLACK, "Insulation jacket", "square"),
        (YELLOW, "Thermocouple", "circle"),
    ]:
        if shape == "circle":
            svg.circle(x + 14, y - 2, 14, color, INK, 2)
        else:
            svg.rect(x, y - 16, x + 28, y + 12, color, INK if color != BLACK else BLACK, 2)
        svg.text(x + 42, y + 4, label, 21)
        x += 360

    col1_x, col2_x, col3_x = 75, 675, 1280
    col_y = 940
    svg.text(col1_x, col_y, "Cell / test notes", 21, "700")
    svg.text(col1_x, col_y + 32, "- C2 = trigger cell", 21)
    svg.text(col1_x, col_y + 60, "- Heaters turned off after C2 entered TR", 21)
    svg.text(col1_x + 24, col_y + 86, "  assumed ~3 s after steepest T7 spike", 19)

    svg.text(col2_x, col_y, "Thermocouple information", 21, "700")
    svg.text(col2_x, col_y + 32, "- Vent area: T3 / T7 / T11 / T15 / T19", 21)
    svg.text(col2_x, col_y + 60, "- Battery surface:", 21)
    svg.text(col2_x + 24, col_y + 86, "  T2 / T4 / T10 / T12 / T14 / T16 / T18 / T20", 19)

    svg.text(col3_x, col_y, "Thermocouple information", 21, "700")
    svg.text(col3_x, col_y + 32, "- Inter-jacket: T5 / T9 / T13 / T17", 21)
    svg.text(col3_x, col_y + 60, "- Heater/jacket: T6 / T8", 21)
    svg.text(col3_x, col_y + 88, "- Outer jacket/air: T1 / T21", 21)


def main():
    OUT_DIR.mkdir(exist_ok=True)
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw_common_png(draw)
    img.save(PNG_OUT)

    svg = Svg()
    draw_svg(svg)
    svg.save(SVG_OUT)
    print(PNG_OUT)
    print(SVG_OUT)


if __name__ == "__main__":
    main()
