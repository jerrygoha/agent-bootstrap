# Installing agent-bootstrap for OpenCode

This adapter installs the shared process-first prompt corpus into OpenCode and points OpenCode at upstream `obra/superpowers` using OpenCode's native plugin mechanism.

## What It Installs

- `~/.config/opencode/opencode.json`
- `~/.config/opencode/agents/*.md`

The generated agent markdown files embed the shared constitution plus the role-specific instructions from this repository.

## Installation

```bash
bash .opencode/install.sh --partner-name "Hun"
```

If you want a custom location:

```bash
bash .opencode/install.sh \
  --partner-name "Hun" \
  --opencode-home "/absolute/path/to/opencode"
```

## Verify

```bash
cat ~/.config/opencode/opencode.json
ls ~/.config/opencode/agents
```

You should see the `superpowers@git+https://github.com/obra/superpowers.git` plugin entry and a generated agent file set.

## Updating

Re-run the installer after pulling the latest repo changes:

```bash
git pull
bash .opencode/install.sh --partner-name "Hun"
```
