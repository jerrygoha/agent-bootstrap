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
  - `shared/agent-metadata.json`
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
- OpenCode uses the native plugin line `superpowers@git+https://github.com/obra/superpowers.git`
- Claude Code is split into:
  - upstream official `superpowers` for the skill library
  - this repository's Claude plugin package for the shared agent prompts

The intent is to reuse upstream superpowers instead of copying their skill library into this repository.

## Install Paths

- Codex: [docs/README.codex.md](docs/README.codex.md)
- Claude Code: [docs/README.claude.md](docs/README.claude.md)
- OpenCode: [docs/README.opencode.md](docs/README.opencode.md)
- OpenClaw integration: [docs/README.openclaw.md](docs/README.openclaw.md)

## Repository Layout

- `AGENTS.md`
  - shared constitution template
- `agents/`
  - shared role prompt bodies
- `shared/agent-metadata.json`
  - shared descriptions and OpenCode capability metadata
- `.codex/`
  - Codex installer, templates, and install guide
- `.opencode/`
  - OpenCode installer, templates, and install guide
- `.claude-plugin/marketplace.json`
  - repository-level Claude marketplace entry
- `plugins/process-first-agents/`
  - generated Claude plugin package
- `scripts/render_claude_plugin.py`
  - rebuilds the Claude plugin package from the shared prompt corpus
- `docs/`
  - harness-specific guides and OpenClaw notes
- `tests/`
  - Python verification for installers and plugin metadata

## Constraints

This repository should contain only the baseline setup that is safe to share publicly.

Keep these out:

- private MCP endpoints
- personal project paths
- organization-specific secrets
- machine-specific trust configuration
- credentials, tokens, or auth state

## Updating

- Codex and OpenCode: re-run the harness installer after pulling
- Claude Code: re-run `python3 scripts/render_claude_plugin.py --partner-name "<Name>"` after pulling, then update the local plugin installation

## Legacy Files

Some files from the earlier Codex-only bootstrap still exist during the transition:

- `codex-home/`
- `scripts/install.py`
- `scripts/install.sh`
- `prompts/fresh-install.md`

They are not the long-term multi-harness entrypoints.

## Testing

Installer and metadata tests use Python's `unittest`:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```
