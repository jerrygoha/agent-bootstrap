# agent-bootstrap

Public bootstrap repository for process-first AI coding environments.

This repository is meant to be the source of truth for a shared operating model that can be installed into multiple coding harnesses instead of being tied to Codex alone.

## Goals

- keep the setup reproducible across machines
- share one process-first prompt corpus across multiple tools
- use each harness's native extension or config mechanism where possible
- keep the partner name configurable during first-time setup
- avoid touching auth, credentials, history, logs, automations, or other runtime state

## First-Class Targets

This repository is designed to support these harnesses directly:

- Codex
- Claude Code
- OpenCode

## Optional Integration Layer

This repository also documents how to plug those harnesses into OpenClaw, but OpenClaw is intentionally not treated as a first-class bootstrap target.

## Architecture

The repository is split into two layers:

- shared core
  - `AGENTS.md`
  - `agents/*.md`
  - common process-first constitution and role prompt bodies
- harness adapters
  - `.codex/`
  - `.claude-plugin/`
  - `.opencode/`

The shared core defines the operating model once.
Each adapter translates that core into the native format expected by the target harness.

## Superpowers Integration

This bootstrap is built around `obra/superpowers`.

- Codex uses the native `~/.agents/skills/superpowers` symlink pattern
- OpenCode uses the native plugin line: `superpowers@git+https://github.com/obra/superpowers.git`
- Claude Code uses native plugin packaging and marketplaces

The intent is to reuse upstream superpowers instead of copying their skill library into this repository.

## Planned Layout

- `AGENTS.md`
  - shared constitution template
- `agents/`
  - shared role prompt bodies
- `.codex/`
  - Codex install docs, templates, and installer
- `.claude-plugin/`
  - Claude Code plugin metadata and marketplace packaging
- `.opencode/`
  - OpenCode install docs, templates, and installer
- `docs/`
  - harness-specific usage and OpenClaw integration notes
- `tests/`
  - installer and metadata verification

## Current Status

The repository is being refactored from a Codex-only bootstrap into the multi-harness structure above.
Until that refactor is complete, some files still live in the old Codex-centric layout.

## Constraints

This repository should contain only the baseline setup that is safe to share publicly.

Keep these out:

- private MCP endpoints
- personal project paths
- organization-specific secrets
- machine-specific trust configuration
- credentials, tokens, or auth state

## Testing

Installer and metadata tests use Python's `unittest`:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```
