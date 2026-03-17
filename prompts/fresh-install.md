You are setting up a fresh Codex environment from this repository.

The repository is the source of truth for a managed subset of `~/.codex`.
Follow these rules exactly:

1. Ask the user what name Codex should use to address them.
   - Default to `Hun` if they do not care.
2. Determine the absolute Codex home path for this machine.
   - Use the normal user home directory and install into `~/.codex`.
   - Resolve it to an absolute path and use that absolute path when rendering templates.
3. Read this repository's `README.md` and inspect `codex-home/`.
4. Treat only these paths as managed install targets:
   - `AGENTS.md`
   - `local.md`
   - `config.toml`
   - `agents/*.md`
5. Before changing any managed target file in `~/.codex`, create a timestamped backup directory and copy the old managed files into it.
6. Render placeholders in the repo templates before installation:
   - replace `{{PARTNER_NAME}}` with the chosen partner name
   - replace `{{CODEX_HOME_ABS}}` with the absolute `~/.codex` path for this machine
7. Install the rendered files into `~/.codex`.
8. Do not modify or delete unrelated `~/.codex` state such as credentials, history, logs, or automations.
9. Verify that:
   - every managed file exists after install
   - `config.toml` points to valid prompt files under the installed `agents/` directory
   - the final setup is internally consistent
10. Summarize:
   - chosen partner name
   - backup location
   - installed files
   - anything skipped or requiring manual follow-up

If any required repo file is missing or malformed, stop and report the issue instead of guessing.
