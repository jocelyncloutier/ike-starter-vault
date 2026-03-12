---
created: 2026-03-11
updated: 2026-03-12
authorship: ai-generated
map: ["[[Getting Started Map]]"]
tags:
  - topic/ike
---
## Context

What this vault is and how to share it with someone else. If you're already here, you've completed setup — this note is useful for passing the vault along to others.

A ready-to-use [Obsidian](https://obsidian.md) vault with a clean folder structure, note templates, and built-in AI support. This vault is pre-configured to work with Claude — so you can have natural-language conversations with your notes from day one. Open it and start capturing — no setup required.
## Step 1 — Get Obsidian

Download and install [Obsidian](https://obsidian.md/download) (free).
## Step 2 — Download the Vault

Click the green **Code** button → **Download ZIP** (last option in the list). Unzip it and rename the folder to `MyVault` (or whatever you'd like to call your vault).

![[github-download.png|800]]

**Create a folder to store your vault, then move it there:**
- **macOS** — Create `~/Obsidian/` in your home folder, then move your vault there: `~/Obsidian/MyVault/`
- **Windows** — Create `C:\Users\YourName\Obsidian\`, then move your vault there: `C:\Users\YourName\Obsidian\MyVault\`

Remember this path — you'll need it in Step 3.

Open Obsidian → **Open folder as vault** → select your vault folder.

![[open-folder-as-vault.png|600]]

When prompted, click **Trust author and enable plugins**.

![[trust-author.png|600]]

A Settings window will open automatically — close it to see your vault.

![[settings-close.png|800]]
## Step 3 — Set Up Claude (Recommended)

This vault includes **Claudian**, a sidebar that lets you chat with Claude directly inside Obsidian. One-time setup:

1. **Install Claude Code** — the engine behind Claudian:
   - macOS: open Terminal, run `curl -fsSL https://claude.ai/install.sh | bash`
   - Windows: open PowerShell, run `irm https://claude.ai/install.ps1 | iex`
2. **Connect to your vault** — in the same terminal, navigate to your vault folder and run `claude`:
   - macOS: `cd ~/Obsidian/MyVault && claude`
   - Windows: `cd C:\Users\YourName\Obsidian\MyVault` then `claude`
3. **Configure Claudian** — once Claude Code is running, type `/setup-claudian`
4. **Close the terminal** — you won't need it again

Claudian is pinned in Obsidian's right sidebar. If you don't see it: Cmd+P → "Claudian."
### Try these first prompts

- *"What's in this vault?"* — Claude will orient you to the structure
- *"Create today's daily note"* — Creates a formatted daily note
- *"Create a note about [something you're thinking about]"* — Claude creates a properly structured note with links
## Learn More

- [Obsidian documentation](https://help.obsidian.md)
- [Claude Code setup guide](https://docs.anthropic.com/en/docs/claude-code/setup)
- New to Obsidian? [This intro video](https://www.youtube.com/watch?v=DbsAQSIKQXk) is a good place to start
