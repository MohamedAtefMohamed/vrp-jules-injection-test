# sha256_util

A simple Python utility for computing SHA-256 hashes of files.

## Features

- Efficient memory usage when hashing large files by reading chunks.
- Command-line interface and Python module API.

## Usage

### Command Line Interface

You can run `sha256_util.py` directly from the command line by passing the path to the file you want to hash:

```bash
python3 sha256_util.py <path_to_file>
```

Example:

```bash
python3 sha256_util.py sample.txt
```

### Python API

You can also import `sha256_file` in your Python code:

```python
from pathlib import Path
from sha256_util import sha256_file

file_path = Path("sample.txt")
file_hash = sha256_file(file_path)
print(f"SHA-256 Hash: {file_hash}")
```

## Running Tests

Install dependencies and run tests using `pytest`:

```bash
pip install -r requirements.txt
python3 -m pytest
```
