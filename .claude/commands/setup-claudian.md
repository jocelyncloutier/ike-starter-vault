Configure the Claudian plugin with Claude Code's CLI path.

## Steps

1. Detect the Claude Code CLI path:
   - macOS/Linux: run `which claude` to get the absolute path
   - Windows: run `where claude` to get the absolute path
2. Read `.obsidian/plugins/claudian/data.json`
3. Set the `clientPath` field to the detected absolute path
4. Write the updated `data.json` back
5. Report the configured path and remind the user to restart Obsidian (or toggle the Claudian plugin off/on in Settings → Community plugins) for the change to take effect

## Notes

- The path must be absolute — no `~` or relative paths
- If `which claude` returns nothing, Claude Code is not installed or not in PATH. Tell the user to install it first: https://docs.anthropic.com/en/docs/claude-code/overview
- This is a one-time setup. After this, use Claudian in Obsidian's sidebar for all AI interactions.
