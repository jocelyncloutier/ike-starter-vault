# IKE Starter Vault

A ready-to-use [Obsidian](https://obsidian.md) vault with a clean folder structure, note templates, and built-in AI. Pre-configured to work with Claude — have natural-language conversations with your notes from day one.

## Prerequisites

1. **Obsidian** — [Download](https://obsidian.md/download) (free)
2. **Claude Desktop** — [Download](https://claude.ai/download) (requires Pro, Max, Teams or Enterprise subscription)

## Install

Open Claude Desktop → **Code** tab

<img src="x/Attachments/Pasted image 20260312154426.png" alt="Claude Desktop Code tab" />

**Paste this prompt:**

> Download the IKE starter vault from https://github.com/jocelyncloutier/ike-starter-vault (zip, main branch). Unzip it to ~/Obsidian/MyVault/ on macOS or C:\Users\%USERNAME%\Obsidian\MyVault\ on Windows. Important: the zip contains hidden directories (.obsidian, .claude) that must be included — use `cp -a` or `rsync -a`, not `cp -R` with a glob. When done, tell me to go back to the README for next steps.

Claude will download and unzip the vault. When it's done, **switch to the vault folder:**

1. Click **New session** in the left sidebar
2. Click the folder name at the bottom-left of the screen
3. Select **Choose a different folder**
4. Navigate to the vault folder (`~/Obsidian/MyVault/`) and select it

The folder name at the bottom-left should now show **MyVault**. Paste this prompt:

> Run `which claude` (macOS/Linux) or `where claude` (Windows) to find the path to the `claude` binary. Open the file `.obsidian/plugins/claudian/data.json` and set the `clientPath` value to that path. Then open the vault in Obsidian by running: `open "obsidian://choose-vault"`

You will see this:

<img src="x/Attachments/Pasted image 20260312172900.png" alt="Obsidian vault chooser" width="600" />

Click on "Open" next to "**Open folder as vault**"
* Select the folder ~/Obsidian/MyVault and click Open button.

Claude configures everything and you create the Obsidian vault from the downloaded folder. Go crazy!

## Why IKE?

Most personal knowledge systems fail because they demand constant maintenance — filing, tagging, linking, formatting. You start strong, then life gets busy, and the system decays.

IKE flips this: **AI does the maintenance.** You capture fast and messy. Claude files your notes, links them to what you already know, surfaces connections you'd miss, and helps you produce outputs — emails, documents, summaries, decisions — from your accumulated knowledge.

- **Capture anything, anywhere** — drop thoughts, web clips, meeting notes, and documents into your inbox. Claude processes them later.
- **Talk to your notes** — ask Claude to summarize, synthesize, draft, research, or find connections across everything in your vault.
- **Never reorganize** — the folder structure is role-agnostic. It survives job changes, career pivots, and shifting interests without restructuring.
- **Zero maintenance** — no tagging rituals, no weekly reviews you'll skip, no filing habits to build. If something needs organizing, ask Claude.

## Learn More

- [Obsidian documentation](https://help.obsidian.md)
- [Claude Code setup](https://docs.anthropic.com/en/docs/claude-code/setup)
- [Obsidian Web Clipper](https://obsidian.md/clipper) — save web pages directly to your vault
