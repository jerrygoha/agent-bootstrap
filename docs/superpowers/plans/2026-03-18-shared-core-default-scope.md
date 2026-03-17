# Shared Core Default Scope Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make `shared-core-only` the default interpretation when a user says "set this up from the repo" without naming a harness, especially for OpenClaw-driven setup flows.

**Architecture:** Keep the change docs-first and prompt-first. Clarify the default scope in the canonical README, split the OpenClaw guide into default shared-core setup vs optional ACP integration, and add copy-paste setup prompts that agents can follow directly without inferring a Codex-first path.

**Tech Stack:** Markdown docs, Python `unittest`

---

### Task 1: Lock the expected shared-core-only behavior in tests

**Files:**
- Modify: `tests/test_shared_core_scope.py`

- [ ] **Step 1: Write the failing assertions**

Add assertions that require:
- `README.md` to mention `shared-core-only` as the default setup scope
- `README.md` to link the shared-core setup prompts
- `docs/README.openclaw.md` to include separate shared-core and ACP paths
- the new prompt files to exist with explicit anti-Codex-first wording

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest discover -s tests -p 'test_shared_core_scope.py'`
Expected: FAIL because the README, OpenClaw guide, and prompt files do not yet match the required wording.

- [ ] **Step 3: Commit**

```bash
git add tests/test_shared_core_scope.py
git commit -m "test: lock shared-core-only default scope"
```

### Task 2: Make shared-core-only explicit in the canonical README

**Files:**
- Modify: `README.md`
- Modify: `README.ko.md`
- Modify: `README.ja.md`
- Modify: `README.zh-CN.md`

- [ ] **Step 1: Add a default scope section to `README.md`**

Document that:
- default scope is `shared-core-only`
- `shared-core-only` means `superpowers` + shared agent/subagent prompts only
- no harness bootstrap is chosen unless the user explicitly asks

- [ ] **Step 2: Surface the setup prompts in `README.md`**

Add a short section linking:
- `prompts/setup-shared-core.md`
- `prompts/setup-openclaw-shared-core.md`
- `prompts/setup-openclaw-acp.md`

- [ ] **Step 3: Mirror the default-scope concept in the translated READMEs**

Add a concise equivalent explanation in:
- `README.ko.md`
- `README.ja.md`
- `README.zh-CN.md`

- [ ] **Step 4: Commit**

```bash
git add README.md README.ko.md README.ja.md README.zh-CN.md
git commit -m "docs: define shared-core-only as default scope"
```

### Task 3: Split the OpenClaw guide into default and optional paths

**Files:**
- Modify: `docs/README.openclaw.md`

- [ ] **Step 1: Rewrite the guide around two explicit paths**

Path A:
- `shared-core-only`
- default for "set this up from the repo"
- no Codex-first assumption

Path B:
- ACP integration
- only if the user explicitly asks for ACP or names a harness

- [ ] **Step 2: Add explicit guardrails**

Document:
- do not default to Codex-first
- do not reset unrelated OpenClaw identity, transport, gateway, or auth settings
- keep ACP work opt-in

- [ ] **Step 3: Commit**

```bash
git add docs/README.openclaw.md
git commit -m "docs: split OpenClaw shared-core and ACP paths"
```

### Task 4: Add copy-paste setup prompts for shared-core-only and ACP

**Files:**
- Create: `prompts/setup-shared-core.md`
- Create: `prompts/setup-openclaw-shared-core.md`
- Create: `prompts/setup-openclaw-acp.md`

- [ ] **Step 1: Write the shared-core-only prompt**

It must:
- default to shared-core-only when no harness is specified
- forbid choosing a harness unless explicitly requested
- define the scope as `superpowers` + shared prompt corpus only

- [ ] **Step 2: Write the OpenClaw shared-core-only prompt**

It must:
- forbid Codex-first by default
- keep unrelated OpenClaw settings untouched
- allow replacing prompt/skill files only within the approved scope

- [ ] **Step 3: Write the OpenClaw ACP prompt**

It must:
- apply only if the user explicitly asks for ACP
- require explicit harness choice before any Codex/Claude/OpenCode bootstrap
- keep unrelated OpenClaw settings untouched

- [ ] **Step 4: Commit**

```bash
git add prompts/setup-shared-core.md prompts/setup-openclaw-shared-core.md prompts/setup-openclaw-acp.md
git commit -m "docs: add shared-core and OpenClaw setup prompts"
```

### Task 5: Verify and finish

**Files:**
- Verify: `tests/test_shared_core_scope.py`
- Verify: `tests/test_*.py`

- [ ] **Step 1: Run targeted scope test**

Run: `python3 -m unittest discover -s tests -p 'test_shared_core_scope.py'`
Expected: PASS

- [ ] **Step 2: Run full test suite**

Run: `python3 -m unittest discover -s tests -p 'test_*.py'`
Expected: PASS

- [ ] **Step 3: Commit**

```bash
git add docs/superpowers/plans/2026-03-18-shared-core-default-scope.md
git commit -m "docs: add shared-core default scope plan"
```
