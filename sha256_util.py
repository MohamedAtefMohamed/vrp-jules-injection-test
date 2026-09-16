#!/usr/bin/env python3
"""Utility for computing SHA-256 hashes of files."""

import hashlib
import sys
from pathlib import Path


def sha256_file(path: Path) -> str:
    """Compute the SHA-256 hash of a file."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: sha256_util.py <file>")
        return 1
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"Error: {path} is not a file")
        return 1
    print(sha256_file(path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
