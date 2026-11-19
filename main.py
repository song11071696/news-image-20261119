#!/usr/bin/env python3
"""news-image-20261119: write the bundled world-news image to /output/entry.png.

The image sums up Thursday 19 November 2026 in one 1024x1024 picture:
the Trump-Xi-Putin trilateral in Shenzhen, GTA VI's worldwide launch,
Anthropic's $83 Nasdaq debut as ANT, Hakeem Jeffries' nomination for
Speaker, the third strike on the Crimean Bridge, and the World Court's
Rohingya verdict — plus a ticker with the record Van Gogh sale, Cyclone
Akvan and the Hormuz tanker mine strikes. Text was composited with PIL
at build time; the background is an AI-generated world map with no text.

Deterministic by construction: this program only copies the bundled
entry.png (same bytes every run). No network, no randomness, no clock.
Standard library only.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = os.environ.get("NEWS_IMAGE_OUTPUT", "/output/entry.png")


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    with open(DST, "rb") as f:
        magic = f.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("output is not a valid PNG: %s" % DST)
    print("wrote %s (%d bytes)" % (DST, os.path.getsize(DST)))


if __name__ == "__main__":
    main()
