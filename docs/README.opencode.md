# OpenCode

OpenCode uses a local installer because the baseline needs user-specific prompt rendering while still relying on upstream `obra/superpowers` through OpenCode's native plugin support.

## Install

```bash
bash .opencode/install.sh --partner-name "Hun"
```

## What It Does

- writes `~/.config/opencode/opencode.json`
- enables the upstream plugin line `superpowers@git+https://github.com/obra/superpowers.git`
- renders the shared constitution plus each role body into `~/.config/opencode/agents/*.md`
- marks review-only agents as read-only where appropriate

## Re-run

```bash
git pull
bash .opencode/install.sh --partner-name "Hun"
```
