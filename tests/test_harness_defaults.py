import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class HarnessDefaultTests(unittest.TestCase):
    def test_main_readme_has_default_scope_matrix(self) -> None:
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("Default Scope Matrix", readme)
        self.assertIn("Codex: `current-harness-only`", readme)
        self.assertIn("Claude Code: `current-harness-only`", readme)
        self.assertIn("OpenCode: `current-harness-only`", readme)
        self.assertIn("OpenClaw: `shared-core-only`", readme)
        self.assertIn("prompts/setup-codex-current-harness.md", readme)
        self.assertIn("prompts/setup-claude-current-harness.md", readme)
        self.assertIn("prompts/setup-opencode-current-harness.md", readme)

    def test_harness_docs_define_current_harness_only_defaults(self) -> None:
        codex_doc = (REPO_ROOT / "docs" / "README.codex.md").read_text(encoding="utf-8")
        claude_doc = (REPO_ROOT / "docs" / "README.claude.md").read_text(encoding="utf-8")
        opencode_doc = (REPO_ROOT / "docs" / "README.opencode.md").read_text(encoding="utf-8")

        self.assertIn("current-harness-only", codex_doc)
        self.assertIn("standing delegation preference", codex_doc)
        self.assertIn("current-harness-only", claude_doc)
        self.assertIn("current-harness-only", opencode_doc)

    def test_openclaw_doc_requires_harness_confirmation_for_acp(self) -> None:
        openclaw_doc = (REPO_ROOT / "docs" / "README.openclaw.md").read_text(encoding="utf-8")

        self.assertIn("native-first", openclaw_doc)
        self.assertIn("ACP is optional", openclaw_doc)
        self.assertIn("ask the user which harness to connect", openclaw_doc)

    def test_current_harness_setup_prompts_exist(self) -> None:
        codex_prompt = (REPO_ROOT / "prompts" / "setup-codex-current-harness.md").read_text(
            encoding="utf-8"
        )
        claude_prompt = (
            REPO_ROOT / "prompts" / "setup-claude-current-harness.md"
        ).read_text(encoding="utf-8")
        opencode_prompt = (
            REPO_ROOT / "prompts" / "setup-opencode-current-harness.md"
        ).read_text(encoding="utf-8")
        openclaw_acp = (REPO_ROOT / "prompts" / "setup-openclaw-acp.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("current-harness-only", codex_prompt)
        self.assertIn("current-harness-only", claude_prompt)
        self.assertIn("current-harness-only", opencode_prompt)
        self.assertIn("Do not configure another harness unless the user explicitly asks.", codex_prompt)
        self.assertIn("Do not configure another harness unless the user explicitly asks.", claude_prompt)
        self.assertIn("Do not configure another harness unless the user explicitly asks.", opencode_prompt)
        self.assertIn("ask the user which harness to connect", openclaw_acp)


if __name__ == "__main__":
    unittest.main()
