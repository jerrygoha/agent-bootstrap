You are setting this repository up for OpenClaw with ACP integration.

Read `README.md` and `docs/README.openclaw.md` first.

Use this mode only if the user explicitly asks for ACP integration or explicitly names a harness.

Follow these rules exactly:

1. Confirm the harness choice before changing anything if it is not already explicit.
2. Apply ACP integration only within the requested scope.
3. Do not modify unrelated OpenClaw settings such as identity, gateway, transport, auth, provider config, or messaging integrations.
4. Back up ACP-related config before editing it.
5. If the user did not explicitly ask for ACP, stop and switch back to `shared-core-only`.
6. Summarize:
   - chosen harness
   - ACP integration changes
   - backup locations
   - anything that still needs manual validation

This path is for ACP integration only if the user explicitly asks for ACP or explicitly names a harness.
