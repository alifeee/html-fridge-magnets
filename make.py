"""Opens `magnets.txt` and creates a PDF file from the contents"""

import csv
from dataclasses import dataclass

FILENAME = "magnets.txt"


@dataclass
class Magnet:
    """A magnet with a HTML fragment"""

    label: str


def read_magnets(file_contents: str) -> list[Magnet]:
    """Reads the magnets from the file content"""
    magnets = []
    file_iterable = file_contents.splitlines()
    reader = csv.DictReader(file_iterable, delimiter=";")
    for row in reader:
        for _ in range(int(row["count"])):
            magnets.append(Magnet(row["text"]))
    return magnets


def main() -> None:
    """Main"""
    with open(FILENAME, "r", encoding="utf-8") as file:
        file_contents = file.read()
    magnets = read_magnets(file_contents)
    print(f"Found {len(magnets)} magnets")


if __name__ == "__main__":
    main()
