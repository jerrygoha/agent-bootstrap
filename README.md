# codex-dotfiles

Public dotfiles for bootstrapping a Codex App or Codex CLI environment.

This repository is the source of truth for a managed subset of `~/.codex`.
It is designed so a fresh Codex session can install the setup safely from this repo.

## Goals

- Keep the setup reproducible across machines
- Preserve a strong process-first workflow built around superpowers
- Keep the user's partner name configurable during first-time install
- Avoid touching auth, credentials, history, logs, automations, or other runtime state

## Managed Files

The installer should manage only these paths under `~/.codex`:

- `AGENTS.md`
- `local.md`
- `config.toml`
- `agents/*.md`

The installer should not modify:

- `.credentials.json`
- `history.jsonl`
- `log/`
- `automations/`
- other unrelated files

## Layout

- `codex-home/`
  - Template content that will be rendered into `~/.codex`
- `prompts/fresh-install.md`
  - Prompt to paste into a fresh Codex session after cloning this repo

## Personalization

Template files may contain these placeholders:

- `{{PARTNER_NAME}}`
- `{{CODEX_HOME_ABS}}`

The fresh-install prompt should ask for the partner name, detect the Codex home path, render the templates, back up any existing managed files, then install the rendered output.

## Usage

1. Clone this repo on a fresh machine.
2. Open Codex in this repository.
3. Paste the contents of `prompts/fresh-install.md`.
4. Let Codex render and install the managed files into `~/.codex`.
