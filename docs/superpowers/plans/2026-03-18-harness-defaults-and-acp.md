# Harness Defaults And ACP Confirmation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make default setup behavior explicit for Codex, Claude Code, OpenCode, and OpenClaw, and require explicit harness confirmation before ACP configuration.

**Architecture:** Keep the change documentation-first. Add a default scope matrix to the main README, tighten harness-specific docs around `current-harness-only` and `shared-core-only`, add copy-paste prompts for Codex/Claude/OpenCode current-harness setup, and document that OpenClaw should stay native-first with ACP only after the user names a harness.

**Tech Stack:** Markdown docs, Python `unittest`

---

### Task 1: Lock the expected default-scope and ACP wording in tests

**Files:**
- Create: `tests/test_harness_defaults.py`

- [ ] **Step 1: Write the failing test**

Add assertions that require:
- `README.md` to include a default scope matrix
- Codex, Claude Code, and OpenCode docs to mention `current-harness-only`
- OpenClaw docs to mention `native-first` plus explicit harness confirmation before ACP
- new prompt files for Codex, Claude Code, and OpenCode setup

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest discover -s tests -p 'test_harness_defaults.py'`
Expected: FAIL because those docs and prompts do not exist yet.

### Task 2: Add the default scope matrix to the canonical README

**Files:**
- Modify: `README.md`
- Modify: `README.ko.md`
- Modify: `README.ja.md`
- Modify: `README.zh-CN.md`

- [ ] **Step 1: Add a table or list describing the default scope by harness**

Required values:
- Codex -> `current-harness-only`
- Claude Code -> `current-harness-only`
- OpenCode -> `current-harness-only`
- OpenClaw -> `shared-core-only`

- [ ] **Step 2: Link the new setup prompts**

Add links to:
- `prompts/setup-codex-current-harness.md`
- `prompts/setup-claude-current-harness.md`
- `prompts/setup-opencode-current-harness.md`
- existing OpenClaw prompts

### Task 3: Tighten harness-specific docs

**Files:**
- Modify: `docs/README.codex.md`
- Modify: `docs/README.claude.md`
- Modify: `docs/README.opencode.md`
- Modify: `docs/README.openclaw.md`

- [ ] **Step 1: Add `current-harness-only` guidance to Codex, Claude, and OpenCode**

Document that a generic repo setup request inside that harness should affect only that harness by default.

- [ ] **Step 2: Add native-vs-ACP guidance to OpenClaw**

Document:
- OpenClaw should stay native-first for default delegation
- ACP is optional
- ACP requires asking the user which harness to connect before any ACP config change

### Task 4: Add harness-specific setup prompts

**Files:**
- Create: `prompts/setup-codex-current-harness.md`
- Create: `prompts/setup-claude-current-harness.md`
- Create: `prompts/setup-opencode-current-harness.md`
- Modify: `prompts/setup-openclaw-acp.md`

- [ ] **Step 1: Add current-harness-only prompts**

Each prompt must:
- default to current-harness-only
- forbid cross-harness setup unless explicitly requested
- preserve unrelated state

- [ ] **Step 2: Tighten the OpenClaw ACP prompt**

Make it explicitly require the user to name the harness before ACP setup proceeds.

### Task 5: Verify and finish

**Files:**
- Verify: `tests/test_harness_defaults.py`
- Verify: `tests/test_*.py`

- [ ] **Step 1: Run targeted test**

Run: `python3 -m unittest discover -s tests -p 'test_harness_defaults.py'`
Expected: PASS

- [ ] **Step 2: Run full suite**

Run: `python3 -m unittest discover -s tests -p 'test_*.py'`
Expected: PASS
