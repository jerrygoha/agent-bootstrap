You are setting this repository up in `shared-core-only` mode.

Read `README.md` first.

Follow these rules exactly:

1. If the user says "set this up from the repo" and does not specify a harness, default to `shared-core-only`.
2. `shared-core-only` means:
   - install or update `superpowers` if the current tool supports it
   - install the shared constitution and agent/subagent prompts in the current tool's native format
   - avoid unrelated runtime reconfiguration
3. Do not choose a harness unless the user explicitly asks for one.
4. Do not redesign ACP, gateway, transport, auth, identity, or provider settings unless the user explicitly asks.
5. Back up or preserve any existing prompt or skills files that will be replaced.
6. Summarize:
   - scope used
   - files backed up
   - files changed
   - anything skipped because the current tool cannot consume it natively

If the repository does not provide a native path for the current tool, stop and say so instead of inventing one.
