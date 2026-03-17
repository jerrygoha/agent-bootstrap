import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class SharedCoreScopeTests(unittest.TestCase):
    def test_main_readme_declares_shared_core_only_default(self) -> None:
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("shared-core-only", readme)
        self.assertIn(
            'If the user says "set this up from the repo" and does not specify a harness, default to `shared-core-only`.',
            readme,
        )
        self.assertIn("prompts/setup-shared-core.md", readme)
        self.assertIn("prompts/setup-openclaw-shared-core.md", readme)

    def test_openclaw_doc_splits_shared_core_and_acp_paths(self) -> None:
        openclaw_doc = (REPO_ROOT / "docs" / "README.openclaw.md").read_text(encoding="utf-8")

        self.assertIn("Path A: shared-core-only", openclaw_doc)
        self.assertIn("Path B: ACP integration", openclaw_doc)
        self.assertIn("Do not default to Codex-first", openclaw_doc)

    def test_setup_prompts_exist_for_shared_core_and_openclaw(self) -> None:
        shared_core = (REPO_ROOT / "prompts" / "setup-shared-core.md").read_text(encoding="utf-8")
        openclaw_shared = (
            REPO_ROOT / "prompts" / "setup-openclaw-shared-core.md"
        ).read_text(encoding="utf-8")
        openclaw_acp = (REPO_ROOT / "prompts" / "setup-openclaw-acp.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("shared-core-only", shared_core)
        self.assertIn("Do not choose a harness unless the user explicitly asks for one.", shared_core)
        self.assertIn("Do not choose Codex-first", openclaw_shared)
        self.assertIn("Do not modify unrelated OpenClaw settings", openclaw_shared)
        self.assertIn("ACP integration", openclaw_acp)
        self.assertIn("only if the user explicitly asks for ACP", openclaw_acp)


if __name__ == "__main__":
    unittest.main()
