You are setting this repository up inside Codex in `current-harness-only` mode.

Read `README.md` and `docs/README.codex.md` first.

Follow these rules exactly:

1. Default to `current-harness-only`.
2. Configure Codex only.
3. Do not configure another harness unless the user explicitly asks.
4. Install or update the Codex-side `superpowers` and shared agent/subagent prompts.
5. Preserve unrelated Codex state such as credentials, history, logs, and automations.
6. Summarize:
   - files changed
   - backups created
   - anything that still needs manual follow-up
