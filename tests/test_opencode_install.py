import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
INSTALLER = REPO_ROOT / ".opencode" / "install.py"


class OpenCodeInstallTests(unittest.TestCase):
    def run_installer(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(INSTALLER),
                "--repo-root",
                str(REPO_ROOT),
                *args,
            ],
            capture_output=True,
            text=True,
        )

    def test_dry_run_reports_opencode_targets_without_writing(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            opencode_home = Path(tmpdir) / "opencode"
            result = self.run_installer(
                "--partner-name",
                "Hun",
                "--opencode-home",
                str(opencode_home),
                "--dry-run",
            )

            self.assertEqual(result.returncode, 0, msg=result.stderr)
            self.assertIn("Dry run:", result.stdout)
            self.assertIn(str(opencode_home.resolve() / "opencode.json"), result.stdout)
            self.assertIn(str(opencode_home.resolve() / "agents" / "eng-lead.md"), result.stdout)
            self.assertFalse(opencode_home.exists())

    def test_install_writes_config_and_rendered_agents(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            opencode_home = Path(tmpdir) / "opencode"
            result = self.run_installer(
                "--partner-name",
                "Hun",
                "--opencode-home",
                str(opencode_home),
            )

            self.assertEqual(result.returncode, 0, msg=result.stderr)
            config = json.loads((opencode_home / "opencode.json").read_text(encoding="utf-8"))
            self.assertEqual(config["$schema"], "https://opencode.ai/config.json")
            self.assertEqual(
                config["plugin"],
                ["superpowers@git+https://github.com/obra/superpowers.git"],
            )
            self.assertEqual(config["default_agent"], "eng-lead")

            eng_lead = (opencode_home / "agents" / "eng-lead.md").read_text(encoding="utf-8")
            reviewer = (opencode_home / "agents" / "reviewer.md").read_text(encoding="utf-8")
            self.assertIn("description: Primary lead for day-to-day work", eng_lead)
            self.assertIn("mode: primary", eng_lead)
            self.assertIn("Hun", eng_lead)
            self.assertIn("description: Review-only work focused on bugs", reviewer)
            self.assertIn("mode: subagent", reviewer)
            self.assertIn("edit: deny", reviewer)


if __name__ == "__main__":
    unittest.main()
