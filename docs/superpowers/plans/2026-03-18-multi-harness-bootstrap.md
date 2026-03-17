# Multi-Harness Bootstrap Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the current Codex-only bootstrap repo into a shared process-first bootstrap repo that supports Codex, Claude Code, and OpenCode as first-class install targets, with OpenClaw documented as an optional integration layer.

**Architecture:** Move the prompt corpus into a shared core, then add harness-specific adapters under `.codex/`, `.claude-plugin/`, and `.opencode/`. Codex and OpenCode get installers plus verification tests; Claude Code gets native plugin marketplace metadata and packaged agent files; OpenClaw gets integration docs only.

**Tech Stack:** Python 3 installer scripts, shell wrappers, Markdown docs/prompts, JSON/TOML config templates, `unittest`, `git`, `gh`

---

### Task 1: Rebrand Repository And Introduce Shared Core

**Files:**
- Create: `AGENTS.md`
- Create: `agents/backend-engineer.md`
- Create: `agents/data-engineer.md`
- Create: `agents/debugger.md`
- Create: `agents/eng-lead.md`
- Create: `agents/frontend-engineer.md`
- Create: `agents/integrations-engineer.md`
- Create: `agents/performance-engineer.md`
- Create: `agents/planner.md`
- Create: `agents/platform-engineer.md`
- Create: `agents/release-manager.md`
- Create: `agents/researcher.md`
- Create: `agents/reviewer.md`
- Create: `agents/security-engineer.md`
- Create: `agents/skill-author.md`
- Create: `agents/verifier.md`
- Create: `agents/worker.md`
- Modify: `README.md`
- Modify: `.gitignore`

- [ ] **Step 1: Write down the shared-core structure in the repo**

Create the shared `AGENTS.md` and `agents/*.md` files by moving the reusable process-first constitution and agent prompt bodies out of the Codex-only template tree.

- [ ] **Step 2: Update the README to describe the new shared-core + harness-adapter architecture**

Run: `sed -n '1,260p' README.md`
Expected: the README no longer describes the repo as Codex-only and instead explains the multi-harness bootstrap model.

- [ ] **Step 3: Verify the shared prompt corpus is present**

Run: `find AGENTS.md agents -maxdepth 2 -type f | sort`
Expected: `AGENTS.md` plus the full shared `agents/*.md` set are listed.

- [ ] **Step 4: Commit the shared-core and rebrand changes**

```bash
git add README.md .gitignore AGENTS.md agents
git commit -m "Rebrand repo around shared agent bootstrap core"
```

### Task 2: Refactor Codex Adapter To Use Shared Core And Native Superpowers Discovery

**Files:**
- Create: `.codex/INSTALL.md`
- Create: `.codex/templates/AGENTS.md`
- Create: `.codex/templates/config.toml`
- Create: `.codex/templates/local.md`
- Modify: `scripts/install.py`
- Modify: `scripts/install.sh`
- Modify: `tests/test_install.py`
- Modify: `README.md`
- Modify: `prompts/fresh-install.md`

- [ ] **Step 1: Write the failing Codex installer tests for the new layout**

Add tests that prove the installer:
- renders from `.codex/templates/`
- installs Codex managed files from the shared core
- creates or refreshes `~/.agents/skills/superpowers` as a symlink to `~/.codex/superpowers/skills`

- [ ] **Step 2: Run the Codex installer tests to confirm they fail first**

Run: `python3 -m unittest discover -s tests -p 'test_*.py'`
Expected: the new Codex-specific assertions fail before implementation.

- [ ] **Step 3: Implement the Codex adapter refactor**

Update the installer and templates so Codex remains fully supported while aligning with the upstream `obra/superpowers` native skill discovery flow.

- [ ] **Step 4: Re-run the Codex installer tests**

Run: `python3 -m unittest discover -s tests -p 'test_*.py'`
Expected: all Codex installer tests pass.

- [ ] **Step 5: Commit the Codex adapter changes**

```bash
git add .codex scripts/install.py scripts/install.sh tests/test_install.py README.md prompts/fresh-install.md
git commit -m "Refactor Codex bootstrap around shared core"
```

### Task 3: Add OpenCode As A First-Class Install Target

**Files:**
- Create: `.opencode/INSTALL.md`
- Create: `.opencode/templates/opencode.json`
- Create: `.opencode/templates/agents/eng-lead.md`
- Create: `.opencode/templates/agents/planner.md`
- Create: `.opencode/templates/agents/debugger.md`
- Create: `.opencode/templates/agents/reviewer.md`
- Create: `.opencode/templates/agents/verifier.md`
- Create: `.opencode/templates/agents/release-manager.md`
- Create: `.opencode/templates/agents/skill-author.md`
- Create: `.opencode/templates/agents/researcher.md`
- Create: `.opencode/templates/agents/worker.md`
- Create: `.opencode/templates/agents/frontend-engineer.md`
- Create: `.opencode/templates/agents/backend-engineer.md`
- Create: `.opencode/templates/agents/platform-engineer.md`
- Create: `.opencode/templates/agents/data-engineer.md`
- Create: `.opencode/templates/agents/security-engineer.md`
- Create: `.opencode/templates/agents/integrations-engineer.md`
- Create: `.opencode/templates/agents/performance-engineer.md`
- Create: `.opencode/install.py`
- Create: `.opencode/install.sh`
- Create: `tests/test_opencode_install.py`
- Modify: `README.md`

- [ ] **Step 1: Write the failing OpenCode installer tests**

Add tests that prove the OpenCode installer:
- writes `~/.config/opencode/opencode.json`
- adds `superpowers@git+https://github.com/obra/superpowers.git` to the plugin array
- installs the shared agent set into `~/.config/opencode/agents/`

- [ ] **Step 2: Run the OpenCode tests to verify they fail first**

Run: `python3 -m unittest discover -s tests -p 'test_*.py'`
Expected: the new OpenCode tests fail before the adapter exists.

- [ ] **Step 3: Implement the OpenCode installer and templates**

Build the OpenCode adapter so it consumes the shared core and emits valid OpenCode config plus markdown agent files with the correct frontmatter.

- [ ] **Step 4: Re-run the full installer test suite**

Run: `python3 -m unittest discover -s tests -p 'test_*.py'`
Expected: Codex and OpenCode installer tests all pass.

- [ ] **Step 5: Commit the OpenCode adapter**

```bash
git add .opencode tests/test_opencode_install.py README.md
git commit -m "Add OpenCode bootstrap adapter"
```

### Task 4: Add Claude Code Plugin Packaging

**Files:**
- Create: `.claude-plugin/plugin.json`
- Create: `.claude-plugin/marketplace.json`
- Create: `docs/README.claude.md`
- Create: `tests/test_claude_plugin_metadata.py`
- Modify: `README.md`

- [ ] **Step 1: Write the failing metadata tests**

Add tests that validate:
- `.claude-plugin/plugin.json` is valid JSON
- `.claude-plugin/marketplace.json` is valid JSON
- the marketplace points at the local plugin source and the plugin name/version match

- [ ] **Step 2: Run tests to watch the Claude metadata assertions fail**

Run: `python3 -m unittest discover -s tests -p 'test_*.py'`
Expected: metadata tests fail until the files exist and match.

- [ ] **Step 3: Implement the Claude plugin packaging metadata and install docs**

Create native Claude plugin metadata and document how the shared prompts fit into the plugin-distributed bootstrap flow.

- [ ] **Step 4: Re-run the full test suite**

Run: `python3 -m unittest discover -s tests -p 'test_*.py'`
Expected: all tests pass, including Claude metadata validation.

- [ ] **Step 5: Commit the Claude adapter**

```bash
git add .claude-plugin docs/README.claude.md tests/test_claude_plugin_metadata.py README.md
git commit -m "Add Claude Code plugin packaging metadata"
```

### Task 5: Document OpenClaw As An Optional Integration Layer

**Files:**
- Create: `docs/README.openclaw.md`
- Modify: `README.md`

- [ ] **Step 1: Write the integration document**

Document OpenClaw as an ACP orchestration layer that can target Codex, Claude Code, or OpenCode backends, without turning it into a first-class bootstrap target.

- [ ] **Step 2: Verify the docs read cleanly**

Run: `sed -n '1,260p' docs/README.openclaw.md`
Expected: the document clearly separates OpenClaw integration from the first-class install targets.

- [ ] **Step 3: Commit the OpenClaw docs**

```bash
git add docs/README.openclaw.md README.md
git commit -m "Document OpenClaw integration layer"
```

### Task 6: Rename The Repository To A Generic Name And Finalize

**Files:**
- Modify: `README.md`
- Modify: `.claude-plugin/plugin.json`
- Modify: `.claude-plugin/marketplace.json`
- Modify: `.codex/INSTALL.md`
- Modify: `.opencode/INSTALL.md`
- Modify: `docs/README.claude.md`
- Modify: `docs/README.openclaw.md`

- [ ] **Step 1: Choose the final generic repository name and update internal links**

Prefer `agent-bootstrap` unless GitHub namespace availability blocks it.

- [ ] **Step 2: Verify repo-wide references**

Run: `rg -n 'codex-dotfiles|jerrygoha/codex-dotfiles' .`
Expected: only intentional migration notes remain.

- [ ] **Step 3: Rename the GitHub repository**

Run: `gh repo rename agent-bootstrap`
Expected: the repository is renamed successfully and the new URL resolves.

- [ ] **Step 4: Run the final verification suite**

Run: `python3 -m unittest discover -s tests -p 'test_*.py'`
Expected: all tests pass on the renamed repository state.

- [ ] **Step 5: Commit any final reference updates and summarize follow-up**

```bash
git add README.md .claude-plugin/plugin.json .claude-plugin/marketplace.json .codex/INSTALL.md .opencode/INSTALL.md docs
git commit -m "Finalize multi-harness bootstrap repo"
```
