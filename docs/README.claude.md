# Claude Code

This repository supports Claude Code in two layers:

- install Anthropic's official `superpowers` plugin for the skills library
- install this repository's `process-first-agents` plugin for the shared agent prompts

## Recommended Setup

1. Install upstream `superpowers` from the official Claude marketplace.
2. Clone this repository locally.
3. Render the Claude plugin bundle with your preferred partner name.
4. Add the local repository as a Claude plugin marketplace.
5. Install `process-first-agents` from that marketplace.

## Render the Plugin Bundle

```bash
python3 scripts/render_claude_plugin.py --partner-name "Hun"
```

This writes:

- `.claude-plugin/marketplace.json`
- `plugins/process-first-agents/.claude-plugin/plugin.json`
- `plugins/process-first-agents/settings.json`
- `plugins/process-first-agents/agents/*.md`

## Install in Claude Code

```text
/plugin marketplace add /absolute/path/to/this/repo
/plugin install process-first-agents@agent-bootstrap
```

## Update

Re-run the renderer after pulling new repo changes, then update the plugin in Claude Code.
