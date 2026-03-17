# Codex

Codex uses a local installer because the baseline needs two things that are user-specific:

- your partner name
- the local `~/.codex` and `~/.agents` paths

## Default Scope

Inside Codex, the default setup scope is `current-harness-only`.

If the user says "set this up from the repo" and does not explicitly ask for Claude Code, OpenCode, OpenClaw ACP, or cross-harness setup, configure Codex only.

Do not configure another harness unless the user explicitly asks.

## Install

```bash
bash .codex/install.sh --partner-name "Hun"
```

## What It Does

- renders `AGENTS.md`, `local.md`, `config.toml`, and `agents/*.md` into `~/.codex`
- syncs the latest upstream `obra/superpowers` into `~/.codex/superpowers`
- creates `~/.agents/skills/superpowers` as a symlink to `~/.codex/superpowers/skills`

## Re-run

```bash
git pull
bash .codex/install.sh --partner-name "Hun"
```
