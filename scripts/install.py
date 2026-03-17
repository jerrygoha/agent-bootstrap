#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

MANAGED_ROOT = "codex-home"
PLACEHOLDER_PATTERN = re.compile(r"\{\{([A-Z0-9_]+)\}\}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render and install the managed Codex dotfiles from this repository."
    )
    parser.add_argument(
        "--partner-name",
        required=True,
        help="Name Codex should use when addressing the user.",
    )
    parser.add_argument(
        "--codex-home",
        default="~/.codex",
        help="Target Codex home directory. Defaults to ~/.codex.",
    )
    parser.add_argument(
        "--repo-root",
        default=None,
        help="Repository root. Defaults to the parent of this script directory.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the install plan without writing or backing up files.",
    )
    return parser.parse_args()


def render_template(content: str, replacements: dict[str, str], source: Path) -> str:
    def replace(match: re.Match[str]) -> str:
        key = match.group(1)
        if key not in replacements:
            raise ValueError(f"unknown placeholder '{key}' in {source}")
        return replacements[key]

    return PLACEHOLDER_PATTERN.sub(replace, content)


def managed_files(template_root: Path) -> list[Path]:
    files: list[Path] = []
    for relative in ("AGENTS.md", "local.md", "config.toml"):
        files.append(template_root / relative)

    agents_dir = template_root / "agents"
    files.extend(sorted(agents_dir.glob("*.md")))
    return files


def backup_existing_files(target_root: Path, managed_relpaths: list[Path]) -> Path | None:
    existing = [target_root / rel for rel in managed_relpaths if (target_root / rel).exists()]
    if not existing:
        return None

    backup_root = (
        target_root
        / "backups"
        / "codex-dotfiles"
        / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    )
    for source in existing:
        destination = backup_root / source.relative_to(target_root)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    return backup_root


def verify_install(target_root: Path, codex_home_abs: str, expected_agent_paths: list[Path]) -> None:
    required_files = [
        target_root / "AGENTS.md",
        target_root / "local.md",
        target_root / "config.toml",
        *expected_agent_paths,
    ]
    missing = [path for path in required_files if not path.exists()]
    if missing:
        missing_str = ", ".join(str(path) for path in missing)
        raise RuntimeError(f"missing installed files: {missing_str}")

    config_text = (target_root / "config.toml").read_text(encoding="utf-8")
    for agent_path in expected_agent_paths:
        expected = f'{codex_home_abs}/agents/{agent_path.name}'
        if expected not in config_text:
            raise RuntimeError(f"config.toml is missing expected agent path: {expected}")


def print_install_plan(target_root: Path, relative_paths: list[Path], partner_name: str) -> None:
    print(f"Dry run: would install managed Codex files into {target_root}")
    print(f"Partner name: {partner_name}")
    print("Managed files:")
    for relative in relative_paths:
        print(f"- {target_root / relative}")


def main() -> int:
    args = parse_args()

    repo_root = Path(args.repo_root).expanduser().resolve() if args.repo_root else Path(__file__).resolve().parents[1]
    template_root = repo_root / MANAGED_ROOT
    if not template_root.is_dir():
        raise SystemExit(f"template root not found: {template_root}")

    target_root = Path(args.codex_home).expanduser().resolve()
    replacements = {
        "PARTNER_NAME": args.partner_name,
        "CODEX_HOME_ABS": str(target_root),
    }

    files = managed_files(template_root)
    relative_paths = [path.relative_to(template_root) for path in files]

    if args.dry_run:
        print_install_plan(target_root, relative_paths, args.partner_name)
        return 0

    backup_root = backup_existing_files(target_root, relative_paths)

    for source in files:
        relative = source.relative_to(template_root)
        destination = target_root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        rendered = render_template(source.read_text(encoding="utf-8"), replacements, source)
        destination.write_text(rendered, encoding="utf-8")

    agent_paths = [path for path in relative_paths if path.parts and path.parts[0] == "agents"]
    verify_install(target_root, str(target_root), [target_root / path for path in agent_paths])

    print(f"Installed managed Codex files into {target_root}")
    print(f"Partner name: {args.partner_name}")
    if backup_root is None:
        print("Backup: no existing managed files were present")
    else:
        print(f"Backup: {backup_root}")
    print("Managed files:")
    for relative in relative_paths:
        print(f"- {target_root / relative}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as err:  # pragma: no cover
        print(f"install failed: {err}", file=sys.stderr)
        raise SystemExit(1)
