import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE_PATH = REPO_ROOT / ".claude-plugin" / "marketplace.json"
PLUGIN_ROOT = REPO_ROOT / "plugins" / "process-first-agents"
PLUGIN_MANIFEST_PATH = PLUGIN_ROOT / ".claude-plugin" / "plugin.json"
PLUGIN_SETTINGS_PATH = PLUGIN_ROOT / "settings.json"


class ClaudePluginTests(unittest.TestCase):
    def test_marketplace_points_at_plugin_package(self) -> None:
        marketplace = json.loads(MARKETPLACE_PATH.read_text(encoding="utf-8"))

        self.assertEqual(marketplace["name"], "agent-bootstrap")
        self.assertEqual(len(marketplace["plugins"]), 1)
        self.assertEqual(marketplace["plugins"][0]["name"], "process-first-agents")
        self.assertEqual(
            marketplace["plugins"][0]["source"],
            "./plugins/process-first-agents",
        )

    def test_plugin_manifest_and_settings_enable_eng_lead(self) -> None:
        manifest = json.loads(PLUGIN_MANIFEST_PATH.read_text(encoding="utf-8"))
        settings = json.loads(PLUGIN_SETTINGS_PATH.read_text(encoding="utf-8"))

        self.assertEqual(manifest["name"], "process-first-agents")
        self.assertEqual(manifest["version"], "1.0.0")
        self.assertEqual(settings, {"agent": "eng-lead"})

    def test_generated_agents_have_frontmatter_and_rendered_constitution(self) -> None:
        eng_lead = (PLUGIN_ROOT / "agents" / "eng-lead.md").read_text(encoding="utf-8")
        reviewer = (PLUGIN_ROOT / "agents" / "reviewer.md").read_text(encoding="utf-8")

        self.assertIn("name: eng-lead", eng_lead)
        self.assertIn("description: Primary lead for day-to-day work", eng_lead)
        self.assertIn("Partner", eng_lead)
        self.assertNotIn("{{PARTNER_NAME}}", eng_lead)
        self.assertNotIn("@local.md", eng_lead)
        self.assertIn("name: reviewer", reviewer)
        self.assertIn("description: Review-only work focused on bugs and regressions", reviewer)


if __name__ == "__main__":
    unittest.main()
