#!/usr/bin/env python3
"""Copy the bundled news image to /output/entry.png.

The image for this entry is stored in the repository as entry.png.
This program copies that file, byte for byte, to the path the
make.fun harness reads. It uses only the Python standard library,
makes no network requests, and produces the same bytes on every run.
"""

import hashlib
import shutil
import sys
from pathlib import Path


def verify_copy(source: Path, destination: Path) -> None:
    """Check the copy is complete before reporting success.

    Exits non-zero with a clear message if the output file is
    missing, has the wrong size, or differs from the source.
    """
    if not destination.exists():
        raise SystemExit(f"error: {destination} was not created")
    if destination.stat().st_size != source.stat().st_size:
        raise SystemExit(
            f"error: size mismatch: {destination} is "
            f"{destination.stat().st_size} bytes, expected "
            f"{source.stat().st_size}"
        )
    source_digest = hashlib.sha256(source.read_bytes()).hexdigest()
    dest_digest = hashlib.sha256(destination.read_bytes()).hexdigest()
    if dest_digest != source_digest:
        raise SystemExit("error: content mismatch after copy")


def main() -> int:
    source = Path(__file__).resolve().parent / "entry.png"
    destination = Path("/output/entry.png")
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)
    verify_copy(source, destination)
    digest = hashlib.sha256(destination.read_bytes()).hexdigest()
    print(f"wrote {destination} ({destination.stat().st_size} bytes)")
    print(f"sha256: {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
