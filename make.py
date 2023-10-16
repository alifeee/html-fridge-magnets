"""Opens `magnets.txt` and creates a PDF file from the contents"""

import csv
from dataclasses import dataclass
import drawsvg as draw

FILENAME = "magnets.txt"


@dataclass
class Magnet:
    """A magnet with a HTML fragment"""

    label: str


def read_magnets(file_contents: str) -> list[Magnet]:
    """Reads the magnets from the file content"""
    magnets = []
    file_iterable = file_contents.splitlines()
    reader = csv.DictReader(file_iterable, delimiter="£")
    for row in reader:
        for _ in range(int(row["count"])):
            magnets.append(Magnet(row["text"]))
    return magnets


def create_svg(magnets: list[Magnet]) -> str:
    """Creates an A4 SVG file from the magnets"""
    # sort magnets by label length
    font_size = 36
    width_multiplier = 20
    magnets.sort(key=lambda x: len(x.label))
    magnets_by_length = {}

    for magnet in magnets:
        length = len(magnet.label)
        if length not in magnets_by_length:
            magnets_by_length[length] = []
        magnets_by_length[length].append(magnet)

    # height is longest label * font size
    longest_label = max(magnets_by_length.keys())
    total_height = longest_label * font_size
    # width is number of different lengths * 20
    total_width = 0
    for length, magnets_bl in magnets_by_length.items():
        total_width += length * width_multiplier

    d = draw.Drawing(width=total_width, height=total_height, origin="top-left")
    # keep track of where we last put something
    cursor = (10, 10)
    for length, magnets_bl in magnets_by_length.items():
        for magnet in magnets_bl:
            print(f"Adding magnet: {magnet.label}")
            # text label
            text = draw.Text(magnet.label, font_size, *cursor, font_family="monospace")
            # add to image
            d.append(text)
            # move cursor
            cursor = (cursor[0], cursor[1] + 10)
        cursor = (cursor[0] + length * width_multiplier, 10)

    text = d.as_svg()
    if text is None:
        raise RuntimeError("Failed to create SVG")
    return text


def main() -> None:
    """Main"""
    with open(FILENAME, "r", encoding="utf-8") as file:
        file_contents = file.read()
    magnets = read_magnets(file_contents)
    print(f"Found {len(magnets)} magnets")

    svg = create_svg(magnets)
    with open("magnets.svg", "w", encoding="utf-8") as file:
        file.write(svg)
    print("Created magnets.svg")


if __name__ == "__main__":
    main()
