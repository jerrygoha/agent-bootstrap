You are setting up a fresh Codex environment from this repository.

The repository is the source of truth for a managed subset of `~/.codex`.
Follow these rules exactly:

1. Read `README.md`.
2. Ask the user what name Codex should use to address them.
   - Default to `Hun` if they do not care.
3. Use the repository installer instead of manually editing files unless the installer is broken.
4. Run:
   - `bash scripts/install.sh --partner-name "<chosen-name>"`
5. Do not modify or delete unrelated `~/.codex` state such as credentials, history, logs, or automations.
6. If the installer fails, inspect `scripts/install.py`, diagnose the actual cause, and fix the smallest reasonable issue before retrying.
7. Summarize:
   - chosen partner name
   - backup location reported by the installer
   - installed files
   - anything skipped or requiring manual follow-up

If any required repo file is missing or malformed, stop and report the issue instead of guessing.
