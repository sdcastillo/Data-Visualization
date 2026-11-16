#!/usr/bin/env python3
"""Count hospital-readmission rows and write the homepage histogram.

The slides draw this file with a bin width of 20 and a horizontal axis
from 0 to 300. This script uses that same cut so the page and the deck
describe one picture. Rows whose readmission count is "Not Available"
are omitted, matching the R Markdown (na = "Not Available").
"""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "hospital_readmission_rates.csv"
SVG_PATH = ROOT / "assets" / "readmissions-histogram.svg"

BIN_WIDTH = 20
X_MAX = 300


def load():
    counts = []
    hospitals_30_50 = set()
    with CSV_PATH.open(newline="") as handle:
        for row in csv.DictReader(handle):
            raw = (row.get("Number of Readmissions") or "").strip()
            if not raw or raw == "Not Available":
                continue
            value = float(raw)
            counts.append(value)
            if 30 <= value <= 50:
                hospitals_30_50.add((row["Hospital Name"], row["State"]))
    return counts, hospitals_30_50


def bins_for(counts):
    bins = [0] * (X_MAX // BIN_WIDTH)
    outside = 0
    for value in counts:
        if value < 0 or value >= X_MAX:
            outside += 1
            continue
        bins[int(value // BIN_WIDTH)] += 1
    return bins, outside


def write_svg(bins):
    width, height = 760, 340
    left, right, top, bottom = 56, 16, 18, 42
    plot_w = width - left - right
    plot_h = height - top - bottom
    peak = max(bins) or 1
    gap = 5
    bar_w = (plot_w - gap * (len(bins) - 1)) / len(bins)

    def y_of(count):
        return top + plot_h - (count / peak) * plot_h

    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img">',
        "<title>Hospital readmission counts, bins of 20, from 0 to 300</title>",
        "<desc>Bar height is the number of hospital-measure rows in each bin. "
        "The 20 to 40 and 40 to 60 bins are marked because they hold the 30 to 50 band discussed in the slides.</desc>",
        '<rect width="100%" height="100%" fill="#ffffff"/>',
    ]
    for tick in (0, 1000, 2000, 3000):
        if tick > peak:
            continue
        y = y_of(tick)
        parts.append(
            f'<line x1="{left}" y1="{y:.1f}" x2="{width - right}" y2="{y:.1f}" stroke="#e5f0ef"/>'
        )
        parts.append(
            f'<text x="{left - 8}" y="{y + 4:.1f}" text-anchor="end" '
            f'font-family="Source Sans 3, Helvetica, sans-serif" font-size="12" fill="#4c6272">{tick:,}</text>'
        )

    for index, count in enumerate(bins):
        x = left + index * (bar_w + gap)
        y = y_of(count)
        start = index * BIN_WIDTH
        # 20–40 and 40–60 are the bins a reader uses to see “about 30 to 50”.
        fill = "#0f5f5b" if start in (20, 40) else "#c5d5df"
        parts.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{top + plot_h - y:.1f}" '
            f'rx="3" fill="{fill}"><title>{start} to {start + BIN_WIDTH}: {count:,} rows</title></rect>'
        )

    axis_y = top + plot_h
    parts.append(
        f'<line x1="{left}" y1="{axis_y:.1f}" x2="{width - right}" y2="{axis_y:.1f}" stroke="#123055"/>'
    )
    for start in (0, 100, 200, 300):
        index = start // BIN_WIDTH
        if start == X_MAX:
            x = left + len(bins) * bar_w + (len(bins) - 1) * gap
        else:
            x = left + index * (bar_w + gap)
        parts.append(
            f'<text x="{x:.1f}" y="{axis_y + 20}" text-anchor="middle" '
            f'font-family="Source Sans 3, Helvetica, sans-serif" font-size="12" fill="#4c6272">{start}</text>'
        )
    parts.append(
        f'<text x="{left + plot_w / 2:.1f}" y="{height - 4}" text-anchor="middle" '
        f'font-family="Source Sans 3, Helvetica, sans-serif" font-size="13" fill="#123055">'
        f"Number of readmissions</text>"
    )
    parts.append(
        f'<text transform="translate(16 {top + plot_h / 2:.1f}) rotate(-90)" text-anchor="middle" '
        f'font-family="Source Sans 3, Helvetica, sans-serif" font-size="13" fill="#123055">'
        f"Hospital–measure rows</text>"
    )
    parts.append("</svg>")
    SVG_PATH.write_text("\n".join(parts) + "\n")


def main():
    counts, hospitals = load()
    bins, outside = bins_for(counts)
    band = sum(1 for value in counts if 30 <= value <= 50)
    write_svg(bins)
    print(f"numeric rows: {len(counts)}")
    print(f"rows with count outside 0–299: {outside}")
    print(f"rows with 30–50 readmissions: {band}")
    print(f"distinct hospitals in that band: {len(hospitals)}")
    for index, count in enumerate(bins):
        start = index * BIN_WIDTH
        print(f"{start:3d}–{start + BIN_WIDTH:<3d} {count}")
    print(f"wrote {SVG_PATH}")


if __name__ == "__main__":
    main()
