# OpenClaw

OpenClaw is treated as an integration layer, not a first-class bootstrap target.

That is intentional.

This repository manages the baseline prompt corpus and harness adapters for:

- Codex
- Claude Code
- OpenCode

OpenClaw should sit on top of those tools after they are installed and verified individually.

## Recommended Order

1. Install and verify one or more first-class harnesses from this repository.
2. Configure OpenClaw ACP agents to launch those installed harnesses.
3. Keep provider-specific OpenClaw settings in your own environment, not in this public repository.

## Why This Repo Does Not Ship OpenClaw Config

OpenClaw provider configuration is environment-specific:

- model/provider selection
- transport and gateway details
- auth and token handling
- local path assumptions

Those do not belong in a public, portable baseline.
