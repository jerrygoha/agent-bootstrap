# Installing agent-bootstrap for Codex

This adapter installs the shared process-first prompt corpus into Codex and wires Codex up to upstream `obra/superpowers` using native skill discovery.

## What It Installs

- `~/.codex/AGENTS.md`
- `~/.codex/local.md`
- `~/.codex/config.toml`
- `~/.codex/agents/*.md`
- `~/.codex/superpowers`
- `~/.agents/skills/superpowers` symlinked to `~/.codex/superpowers/skills`

## Installation

```bash
bash .codex/install.sh --partner-name "Hun"
```

If you want custom locations:

```bash
bash .codex/install.sh \
  --partner-name "Hun" \
  --codex-home "/absolute/path/to/.codex" \
  --agents-home "/absolute/path/to/.agents"
```

## Verify

```bash
ls -la ~/.agents/skills/superpowers
```

You should see a symlink pointing at `~/.codex/superpowers/skills`.

## Updating

Re-run the installer after pulling the latest repo changes:

```bash
git pull
bash .codex/install.sh --partner-name "Hun"
```
