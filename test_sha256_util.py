#!/usr/bin/env python3
"""Tests for sha256_util."""

import hashlib
from pathlib import Path

from sha256_util import sha256_file


def test_sha256_known_value(tmp_path: Path) -> None:
    f = tmp_path / "hello.txt"
    f.write_text("hello world")
    expected = hashlib.sha256(b"hello world").hexdigest()
    assert sha256_file(f) == expected


def test_sha256_empty_file(tmp_path: Path) -> None:
    f = tmp_path / "empty.txt"
    f.write_bytes(b"")
    expected = hashlib.sha256(b"").hexdigest()
    assert sha256_file(f) == expected


def test_sha256_large_file(tmp_path: Path) -> None:
    f = tmp_path / "large.bin"
    f.write_bytes(b"x" * 200000)
    expected = hashlib.sha256(b"x" * 200000).hexdigest()
    assert sha256_file(f) == expected
