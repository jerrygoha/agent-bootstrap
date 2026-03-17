#!/usr/bin/env python3

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    installer = repo_root / ".codex" / "install.py"
    result = subprocess.run(
        [sys.executable, str(installer), *sys.argv[1:]],
        cwd=repo_root,
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
