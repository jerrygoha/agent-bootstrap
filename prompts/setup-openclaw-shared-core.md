You are setting this repository up for OpenClaw in `shared-core-only` mode.

Read `README.md` and `docs/README.openclaw.md` first.

Follow these rules exactly:

1. Goal: install `superpowers` plus the shared agent/subagent prompt layer only.
2. This is not a full OpenClaw reset.
3. Do not choose Codex-first, Claude-first, or OpenCode-first by default.
4. Do not modify unrelated OpenClaw settings such as identity, gateway, transport, auth, provider config, or messaging integrations.
5. Replace or remove existing prompt/skill files only inside the approved shared-core scope, and back them up first.
6. Do not touch ACP settings unless the user explicitly asks for ACP integration.
7. Summarize:
   - backup locations
   - prompt/skill files changed
   - anything that requires a manual follow-up

If you cannot map the repository's shared core into the current OpenClaw environment confidently, stop and explain what is missing.
