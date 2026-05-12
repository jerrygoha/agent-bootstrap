# Agent Stack Modernization Design

Date: 2026-05-12

## Context

This repository bootstraps Hun's coding-agent environment across Codex, Claude Code, and OpenCode. The current machine and repository are out of sync with the current toolchain:

- Local Codex CLI is `0.128.0`; npm reports `@openai/codex` latest as `0.130.0`.
- Local Claude Code is `2.1.47`; npm reports `@anthropic-ai/claude-code` latest as `2.1.139`.
- Local manual `~/.codex/superpowers` is on commit `917e5f53b16b115b70a3a355ed5f4993b9f8b73d`; upstream `obra/superpowers` `main` is `f2cbfbefebbfef77321e4c9abc9e949826bea9d7`, with latest tag `v5.1.0`.
- The Codex curated `superpowers` plugin cache already reports version `5.1.0`, so this machine currently has both curated-plugin and manual-symlink discovery paths available.
- Repository Codex templates still default to `gpt-5.4`.
- Claude plugin metadata still contains stale `jerrygoha` identity values.
- The current Codex installer can force-reset the manual Superpowers checkout and replace the `~/.agents/skills/superpowers` path without first proving that doing so is safe.
- Root AGENTS instructions currently contain an ask-versus-act conflict: one rule says to always stop for clarification, while the proactiveness rule says to proceed unless a meaningful decision is blocked.

The update should improve both the live local environment and the reusable bootstrap artifacts in this repository.

## Goals

- Update Hun's local Codex, Claude Code, and manual Superpowers installation to the latest confirmed versions.
- Make `gpt-5.5` the default Codex model and keep `gpt-5.4` as the explicitly supported previous-model fallback.
- Ensure spawned Codex agents follow the same default model policy as root Codex sessions.
- Modernize Codex templates around the current config reference where doing so is low risk.
- Improve AGENTS/local prompt templates and role prompts by removing conflicts and aligning them with current Codex and Claude Code agent behavior.
- Update Claude plugin metadata and generated files to use `hun99999` identity values.
- Add Claude plugin subagent frontmatter that prevents read-only roles from inheriting write-capable tools.
- Make local Superpowers update behavior fail closed instead of force-resetting or replacing user-managed paths.
- Clarify Superpowers installation so users understand official plugin versus manual fallback behavior.
- Add tests that prevent stale model defaults, stale GitHub identity values, and broken generated plugin metadata from returning.

## Non-Goals

- Do not rewrite the whole prompt corpus.
- Do not delete user data or private repository content.
- Do not remove backward compatibility for existing manual Superpowers installs unless Hun approves that specific removal.
- Do not hardcode Claude model IDs unless the current Claude Code docs or CLI clearly confirm the exact latest and previous model aliases.
- Do not add a Codex legacy/new-agent compatibility bridge without explicit approval from Hun. If migration cannot be proven safe, stop and report the blocker instead of silently supporting both formats.
- Do not use `git reset --hard` as the normal Superpowers update path.
- Do not remove or replace a non-matching `~/.agents/skills/superpowers` path without explicit approval from Hun.
- Do not bypass pre-commit hooks or skip test output review.

## Design

### Local Environment

Update local global npm tools using the existing Node environment:

- `@openai/codex@latest`
- `@anthropic-ai/claude-code@latest`

Refresh the manual Superpowers checkout by fetching upstream and moving it to the current upstream default branch. Verify with:

- `codex --version`
- `claude --version`
- `git -C ~/.codex/superpowers status --short`
- `git -C ~/.codex/superpowers rev-parse HEAD`

The manual Superpowers checkout must be updated safely:

- If `~/.codex/superpowers` does not exist, clone the configured remote.
- If it exists and is a git checkout with the expected remote, fetch the upstream default branch and fast-forward only.
- If it is dirty, has local commits that cannot fast-forward, has a different remote, or is not a git checkout, stop and report the exact state.
- Do not force-reset, delete, or replace it during the normal update path.

Because Codex already has the curated `superpowers` plugin cached, do not delete the manual `~/.agents/skills/superpowers` symlink in this pass. Document the duplicate-loading risk and make repository behavior explicit. If `~/.agents/skills/superpowers` already points somewhere else or is a real directory, the installer should stop with a clear message rather than replacing it.

### Codex Models and Config

Repository Codex templates should default to:

```toml
model = "gpt-5.5"
model_reasoning_effort = "xhigh"
model_reasoning_summary = "detailed"
model_verbosity = "high"
plan_mode_reasoning_effort = "xhigh"
```

They should also include a profile for the previous model:

```toml
[profiles.previous]
model = "gpt-5.4"
```

The top-level default is the strongest current model. The `previous` profile is the escape hatch for quota, latency, regressions, or model availability issues.

All default Codex execution paths, including spawned agents, must use `gpt-5.5` unless the `previous` profile is selected or a role has an explicitly justified model override. Existing per-agent `model = "gpt-5.4"` pins must not remain in default agent definitions.

The previous-model profile is intended for the whole session. If the final config shape pins spawned agents to `gpt-5.5`, `--profile previous` may only downgrade the root session. That is not acceptable unless it is documented as a known limitation and approved before implementation.

Codex agent-role configuration should be modernized only after tests capture the expected config shape and the updated local Codex runtime proves the shape loads correctly. The preferred target is the current `[agents.<name>]` role format from the Codex config reference:

```toml
[agents.reviewer]
description = "Review-only work focused on bugs, regressions, missing tests, and operational risk."
config_file = "agents/reviewer.toml"
```

The role config file must point at the existing prompt body through a currently supported Codex config key. The implementation must verify the exact key before using it. Candidate keys must not be invented.

Migration matrix:

| Current legacy shape | Target shape | Verification |
| --- | --- | --- |
| `[[custom_agent]].agent_type` | `[agents.<name>]` table name | generated config exposes each expected role name |
| `[[custom_agent]].description` | `agents.<name>.description` | config test checks non-empty descriptions |
| `base_instructions_file = "{{CODEX_HOME_ABS}}/agents/<role>.md"` | `agents.<name>.config_file = "agents/<role>.toml"` plus a verified role config key that loads the same prompt file | post-update smoke check proves the role uses the intended prompt |
| `sandbox_mode`, `approval_policy`, `model_reasoning_effort` | role config file fields, if supported by the current schema | schema/config-load check proves the fields are accepted |
| `orchestrator` alias pointing at `eng-lead.md` | explicit alias role pointing at the same role config file | tests allow only this duplicate prompt target |

If the updated local Codex runtime cannot prove `[agents.<name>]` support for this bootstrap, stop and ask Hun whether to keep legacy `[[custom_agent]]` for this pass. Do not silently keep both legacy and new role registration for the same names.

### Claude Code Agents

Regenerate the Claude plugin with updated metadata:

- author name should be `Hun`
- author email should use `48903443+hun99999@users.noreply.github.com`
- repository should be `https://github.com/hun99999/agent-bootstrap`

Claude agent frontmatter should be improved conservatively:

- use `model: inherit` explicitly for every generated Claude plugin agent
- use `disallowedTools` for read-only roles so they do not inherit write-capable tools
- use `isolation: worktree` for write-capable specialist roles that may edit independently
- do not add `effort` or `maxTurns` in this pass unless Hun approves concrete role/value pairs

This avoids inventing Claude model names while still adopting current Claude Code agent features.

Initial Claude role policy:

| Role category | Roles | Frontmatter policy |
| --- | --- | --- |
| Main lead | `eng-lead` | `model: inherit`; no worktree isolation by default |
| Read-only or gatekeeping | `planner`, `researcher`, `debugger`, `reviewer`, `verifier`, `release-manager` | `model: inherit`; `disallowedTools` must block write/edit tools after confirming exact Claude tool names |
| Write-capable specialists | `worker`, `frontend-engineer`, `backend-engineer`, `platform-engineer`, `data-engineer`, `security-engineer`, `integrations-engineer`, `performance-engineer`, `skill-author` | `model: inherit`; `isolation: worktree` |

Plugin-ignored fields such as `hooks`, `mcpServers`, and `permissionMode` must not be emitted into plugin subagent frontmatter.

### Prompt Corpus

Prompt changes should be narrow and behavior-driven:

- Keep the Hun/Bot working relationship and honesty rules.
- Preserve TDD, verification, git safety, and root-cause debugging requirements.
- Replace the absolute "always ask for clarification" rule with scoped wording: ask only when ambiguity would change scope, safety, architecture, destructive actions, or correctness; otherwise state the assumption briefly and proceed.
- Keep the standing preference that subagents may be used for independent work when the current host/runtime exposes that capability. If unavailable or restricted, stay local and say so.
- Qualify journal/memory instructions by host capability. Use the host's journal or memory mechanism when available; do not invent files or commits for journaling unless the repo or workflow defines them.
- Collapse repeated anti-sycophancy language into one concise rule that requires direct technical judgment and pushback when needed.
- Allow the debugger role to continue into TDD implementation when Hun asked for a fix and the host permits edits; keep read-only handoff behavior for investigation-only tasks.
- Remove stale username and repository references.

The goal is shorter, clearer operating policy, not a larger prompt.

### Superpowers Documentation

Docs should explain the current split plainly:

- Codex App can use the official curated Superpowers plugin.
- The installer can still maintain a manual `~/.codex/superpowers` checkout for environments that rely on local skill discovery.
- Users should avoid enabling both discovery paths unless they intentionally want duplicate skill entries.
- OpenCode continues to use its own native `superpowers@git+https://github.com/obra/superpowers.git` plugin line and is separate from Codex curated-plugin/manual-symlink behavior.

The implementation should prefer explicit documentation and tests before changing destructive local state.

Codex installer behavior should remain manual-compatible, but explicit:

- Keep manual Superpowers install support.
- Add a flag such as `--superpowers-mode manual|skip`.
- Preserve current manual mode unless Hun approves changing the default.
- Warn when a Codex curated Superpowers plugin cache is detected and manual skill symlink installation may create duplicate skill entries.

### Tests and Verification

Add or update tests to check:

- Codex templates default to `gpt-5.5`.
- Codex templates expose a `gpt-5.4` previous-model profile.
- Codex templates include `model_reasoning_summary = "detailed"`, `model_verbosity = "high"`, and `plan_mode_reasoning_effort = "xhigh"`.
- `gpt-5.4` appears only in the intended previous profile unless Hun approves a role-specific fallback pin.
- `.codex/templates/config.toml` and `codex-home/config.toml` stay consistent.
- The installed temp Codex config rendered by `.codex/install.py` follows the same model and agent-shape policy.
- Generated Claude plugin metadata uses `hun99999` values.
- The Claude plugin renderer, not only checked-in generated JSON, emits the updated identity values.
- Generated Claude plugin agents include expected `model: inherit`, read-only tool denial, write-capable isolation, and no plugin-ignored fields.
- Repository files no longer contain stale `jerrygoha` or `Jerry Go` references, except in historical docs where explicitly allowed.
- Installer/docs still describe Superpowers behavior consistently.
- Prompt policy tests assert that absolute clarification wording is gone, subagent permission is host-capability-gated, and journal/memory requirements are host-capability-gated.
- Superpowers docs tests cover README, translated READMEs, `docs/README.codex.md`, and `.codex/INSTALL.md`.

The stale identity allowlist is limited to dated historical planning/spec files under `docs/superpowers/plans/**` and `docs/superpowers/specs/**`. Active docs, renderer code, generated plugin files, README files, installer docs, and `docs/repo-metadata.md` are not allowlisted.

Translated README variants are public-facing docs and must be updated in the same implementation patch as the English docs.

Run the repository test suite after implementation and read the full output.

## Rollout

1. Commit this revised design after subagent findings are incorporated.
2. After Hun reviews the revised design, write an implementation plan.
3. Record current local versions and local Superpowers git status.
4. Update local npm tools and verify actual versions.
5. Update the manual Superpowers checkout only if it can fast-forward safely.
6. Add failing tests for the repository policy changes.
7. Implement repository changes in the smallest coherent patches.
8. Regenerate derived Claude plugin files.
9. Run tests and stale-string checks.
10. Commit the completed changes.
11. Apply GitHub repository metadata only after `gh repo view hun99999/agent-bootstrap` confirms the target.

## Open Decisions

- Whether to remove the local `~/.agents/skills/superpowers` symlink in a later pass after confirming the curated plugin path is active. This pass keeps it and documents duplicate-loading risk.
- Whether to fully migrate Codex custom agents to `[agents.<name>]` in this pass. The default is to attempt migration only after local update and smoke validation; if validation fails, stop and ask Hun before retaining legacy or adding any compatibility bridge.
