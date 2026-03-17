# OpenClaw

OpenClaw is still treated as an integration layer rather than a first-class bootstrap target.

That part has not changed.

What has changed is the default setup scope.

If a user says "set this up from the repo" and does not explicitly ask for ACP or name a harness, the correct default is `shared-core-only`.

Do not default to Codex-first.

## Native Vs ACP

OpenClaw should stay `native-first` for default delegation.

ACP is optional.

Use OpenClaw-native delegation for routine internal orchestration. Use ACP only when the user explicitly wants an external harness runtime such as Codex, Claude Code, or OpenCode.

## Path A: shared-core-only

This is the default path for OpenClaw users who want the repository's workflow layer without replacing the rest of their OpenClaw environment.

Use this path when the user wants:

- `superpowers`
- shared prompt corpus
- agent and subagent prompts
- minimal disruption to their existing OpenClaw setup

What to do:

- install or update `superpowers` if the current environment supports it
- apply `AGENTS.md` and `agents/*.md` in whatever native format the current OpenClaw setup can consume
- back up any prompt or skill files you replace

What not to do:

- do not choose Codex-first, Claude-first, or OpenCode-first by default
- do not change ACP settings
- do not touch unrelated OpenClaw identity, gateway, transport, auth, or provider settings
- do not reset the entire OpenClaw environment

## Path B: ACP integration

This is the optional path.

Use it only if the user explicitly asks for ACP integration or explicitly names a harness such as Codex, Claude Code, or OpenCode.

What to do:

- ask the user which harness to connect if that is not already explicit
- identify the requested harness explicitly
- bootstrap that harness only if the user asked for it
- configure OpenClaw ACP settings only within that requested integration scope
- back up ACP-related config before editing it

What not to do:

- do not infer ACP from a generic setup request
- do not change unrelated OpenClaw identity, gateway, transport, auth, or provider settings
- do not treat a repo URL alone as permission to redesign the user's runtime stack

## Recommended Order

For generic setup requests:

1. Start with Path A: `shared-core-only`
2. Stop there unless the user asks for ACP or names a harness

For explicit ACP requests:

1. Confirm the harness
2. Bootstrap that harness if needed
3. Apply only the ACP integration changes required for that harness

## Scope Boundary

This repository does not ship a universal OpenClaw config because those settings are environment-specific:

- model/provider selection
- transport and gateway details
- auth and token handling
- local path assumptions

Those should remain in the user's own environment unless they explicitly request changes inside that scope.
