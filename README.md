# codex-dotfiles

Public dotfiles for bootstrapping a Codex App or Codex CLI environment.

This repository is the source of truth for a managed subset of `~/.codex`.
It is designed so a fresh Codex session, or a user running a script directly, can install the setup safely from this repo.

## Goals

- Keep the setup reproducible across machines
- Preserve a strong process-first workflow built around superpowers
- Keep the partner name configurable during first-time install
- Avoid touching auth, credentials, history, logs, automations, or other runtime state
- Make installation safe enough to re-run on an existing machine

## What This Repository Manages

The installer manages only these paths under `~/.codex`:

- `AGENTS.md`
- `local.md`
- `config.toml`
- `agents/*.md`

These files define:

- the global working rules
- the multi-agent role prompts
- the process-first Codex configuration

## What It Intentionally Does Not Manage

The installer does not modify:

- `.credentials.json`
- `history.jsonl`
- `log/`
- `automations/`
- private machine-specific files that are unrelated to the managed setup
- per-user MCP credentials or private project trust lists

This repository is a portable baseline, not a full machine image.

## Repository Layout

- `codex-home/`
  - Template content that gets rendered into `~/.codex`
- `codex-home/agents/`
  - Role prompts for the process and domain agents
- `scripts/install.py`
  - Main installer that renders placeholders, backs up managed files, installs the rendered output, and verifies the result
- `scripts/install.sh`
  - Small shell wrapper around `install.py`
- `prompts/fresh-install.md`
  - Prompt to paste into a fresh Codex session after cloning this repo

## Personalization

Template files may contain these placeholders:

- `{{PARTNER_NAME}}`
- `{{CODEX_HOME_ABS}}`

At install time:

- `{{PARTNER_NAME}}` is replaced with the chosen partner name
- `{{CODEX_HOME_ABS}}` is replaced with the resolved absolute `~/.codex` path

The partner name is intentionally not hardcoded.
The installer should ask for it during first-time setup.
If the user does not care, the default is `Hun`.

## Install Methods

### Method 1: Use Codex to install from this repo

1. Clone this repo on a fresh machine.
2. Open Codex App or Codex CLI in this repository.
3. Paste the contents of `prompts/fresh-install.md`.
4. Let Codex ask for the partner name and run the installer.

### Method 2: Run the installer directly

```bash
bash scripts/install.sh --partner-name "Hun"
```

If you want a different Codex home location:

```bash
bash scripts/install.sh --partner-name "Hun" --codex-home "/absolute/path/to/.codex"
```

## Installer Behavior

The installer will:

1. Resolve the target Codex home directory.
2. Back up any currently managed files into a timestamped backup directory under `~/.codex/backups/codex-dotfiles/`.
3. Render template placeholders from `codex-home/`.
4. Install the rendered files into `~/.codex`.
5. Verify that all managed files exist and that `config.toml` references the installed agent prompt files.

The installer does not delete unrelated files from `~/.codex`.

## Updating an Existing Machine

Re-run the installer after pulling the latest changes:

```bash
git pull
bash scripts/install.sh --partner-name "Hun"
```

Because the installer only manages a known subset of files and creates backups first, this is safe to repeat.

## Operating Model

This setup is intentionally process-first.

The top-level pattern is:

- `eng-lead` decides whether work stays local or is delegated
- `planner`, `debugger`, `reviewer`, `verifier`, and `release-manager` enforce process
- domain agents like `frontend-engineer` and `backend-engineer` implement specialized work

The default bias is:

- local execution first
- delegation only when it creates clear leverage
- superpowers process always

## Notes for Extending This Repository

If you add new managed files:

- put templates under `codex-home/`
- keep placeholders explicit
- update the installer verification logic if needed
- update this README
- update `prompts/fresh-install.md` if the installation flow changes
