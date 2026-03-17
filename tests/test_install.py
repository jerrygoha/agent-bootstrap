import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
INSTALLER = REPO_ROOT / "scripts" / "install.py"


class InstallScriptTests(unittest.TestCase):
    def test_dry_run_reports_managed_files_without_writing(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            codex_home = Path(tmpdir) / ".codex"
            result = subprocess.run(
                [
                    sys.executable,
                    str(INSTALLER),
                    "--repo-root",
                    str(REPO_ROOT),
                    "--partner-name",
                    "Hun",
                    "--codex-home",
                    str(codex_home),
                    "--dry-run",
                ],
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0, msg=result.stderr)
            self.assertIn("Dry run:", result.stdout)
            self.assertIn(str(codex_home / "config.toml"), result.stdout)
            self.assertFalse(codex_home.exists())


if __name__ == "__main__":
    unittest.main()
