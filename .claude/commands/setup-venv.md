Set up the Python virtual environment for this vault.

**Detect the platform first** (macOS/Linux vs Windows) and adapt all paths and commands accordingly.

**Determine the venv path:** The venv lives at the vault root. Detect the vault root (the current working directory) and set the venv path as `<vault-root>/.venv`.

## Platform Paths

Use `VENV` below as shorthand for the derived `<vault-root>/.venv` path.

| | macOS/Linux | Windows |
|---|---|---|
| `uv` binary (after install) | `~/.local/bin/uv` | `%USERPROFILE%\.local\bin\uv.exe` |
| Venv location | `<vault-root>/.venv` | `<vault-root>\.venv` |
| Python binary | `<vault-root>/.venv/bin/python3` | `<vault-root>\.venv\Scripts\python.exe` |

## Steps

1. Determine the venv path: resolve the vault root (current working directory), then set `VENV` to `<vault-root>/.venv`. Print the resolved path so the user can see it.

2. Check if `uv` is already installed by running `uv --version`. If that fails, install it:
   - macOS/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
   - Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
   - After install, reference `uv` by its full path (see table above) — it won't be on PATH until the next shell session.

3. Create the venv with Python 3.13:
   ```
   uv venv --python 3.13 --allow-existing $VENV
   ```
   This auto-downloads Python 3.13 if it's not already installed. No Homebrew, system Python, or Xcode needed. The `--allow-existing` flag makes this safe to re-run.

4. Install packages from the vault's `requirements.txt`:
   ```
   VIRTUAL_ENV=$VENV uv pip install -r requirements.txt
   ```
   On Windows, set the environment variable first: `$env:VIRTUAL_ENV="..."` then run `uv pip install`.

5. Verify the venv works:
   ```
   $VENV/bin/python3 --version
   ```
   Expected output: `Python 3.13.x`

6. Verify the permission rule `"Bash(.venv/bin/python3 *)"` exists in `.claude/settings.json`. It ships pre-configured — if it's already there, do nothing. If missing, add it to the `permissions.allow` array.

7. Test the note formatter:
   ```
   $VENV/bin/python3 x/scripts/format-note.py --dry-run "Atlas/Notes/Getting Started.md"
   ```

8. Report success. Tell the user the venv path and that the formatter is ready to use.

## Notes

- The venv lives at the vault root — gitignored and excluded from Obsidian Sync
- `uv` is a standalone tool by Astral that manages Python versions and packages — no prerequisites beyond curl (macOS) or PowerShell (Windows)
- This is a one-time setup. Packages can be updated later by re-running this command.
- If `uv` is already installed and the venv already exists, this command will update packages from `requirements.txt` without recreating anything.
