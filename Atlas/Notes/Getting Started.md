---
created: 2026-03-10
updated: 2026-03-12
authorship: ai-generated
map: ["[[Getting Started Map]]"]
tags:
  - topic/ike
---
> First steps after opening this vault. Work through these in order.
## Step 1 — Look Around

You're in Obsidian. The left sidebar shows your vault's folder structure (Notebook Navigator). The calendar widget at the top lets you create daily notes by clicking a date.

Click through the folders to see how they're organized:
- **`+/`** — Your inbox. Everything lands here first.
- **`Atlas/`** — Your knowledge base. Maps, notes, and reference material.
- **`Calendar/`** — Daily notes, weekly and monthly reviews.
- **`Efforts/`** — Active projects and work.
- **`x/`** — Templates, attachments, and infrastructure.

See [[IKE Vault Guide]] for the full explanation of each folder.
## Step 2 — Understand How Notes Work

Every note has **frontmatter** — a YAML block at the top that stores metadata (creation date, authorship, tags). In reading view, frontmatter is hidden. To see it:
- **Source mode** — click the book/code icon in the top-right of any note
- **File Properties panel** — click the `i` icon in the right sidebar

Try it: open `Calendar/2026-03-10.md` and switch to source mode to see the frontmatter.
## Step 3 — Set Up Claude (Your AI Assistant)

Claude is the AI that helps you manage this vault — creating notes, filing captures, finding connections, drafting emails, and more. You interact with Claude through **Claudian**, a chat sidebar built into Obsidian. You never need to learn the terminal.

**3a — Install Claude Code**

Claude Code is the engine that powers Claudian. Install it once:
- **macOS:** Open Terminal, paste this, press Enter:
  ```
  curl -fsSL https://claude.ai/install.sh | bash
  ```
- **Windows:** Open PowerShell, paste this, press Enter:
  ```
  irm https://claude.ai/install.ps1 | iex
  ```

When prompted, log in with your Claude account (requires a Pro, Max, or Teams subscription).

To verify it installed correctly, type `claude doctor` and press Enter. You should see a success message.

**3b — Connect Claude to Your Vault**

Still in the terminal, navigate to your vault folder and start Claude Code:
- **macOS:**
  ```
  cd ~/Obsidian/MyVault
  claude
  ```
- **Windows:**
  ```
  cd C:\Users\YourName\Obsidian\MyVault
  claude
  ```

Replace `MyVault` with whatever you named your vault folder when you unzipped it. This must be the same folder you opened in Obsidian.

**3c — Configure Claudian**

Once Claude Code is running in your terminal, type:
```
/setup-claudian
```

This tells Claude Code to find its own path and write it into Claudian's settings. You'll see a confirmation message with the path it configured.

**3d — Close the Terminal**

You're done with the terminal. Close it. From now on, you use **Claudian** inside Obsidian for all AI interactions.
## Step 4 — Open Claudian

In Obsidian, look for the Claudian tab in the right sidebar (it should already be pinned there with a bot icon). If you don't see it, use the command palette: **Cmd+P** (macOS) or **Ctrl+P** (Windows) → type "Claudian" → select "Open Claudian."

Try these first conversations:
- **"What's in this vault?"** — Claude will orient you to the structure
- **"Create today's daily note"** — Creates a formatted daily note with the right template
- **"Create a note about [something you're thinking about]"** — Claude creates a properly structured note with frontmatter and links

Claude reads the vault's configuration file (`.claude/CLAUDE.md`) automatically. It already knows your folder structure, templates, and conventions. Over time, you can customize that file to teach Claude about your role, tools, and preferences — but that's optional and you don't need to touch it now.
## Step 5 — Try the Inline Comment Workflow

Open any note and add a comment like this: `%%rewrite this section to be more concise%%`

Then tell Claude: "Review the comments in [note name]." Claude will find every `%%comment%%`, apply the requested changes, and remove the markers.

This is the core IKE editing pattern — you batch your feedback, then Claude processes it all at once.
## Step 6 — Create Your First Effort

An Effort is a project or piece of work you're actively doing. Ask Claude: "Create an effort note for [your project]." Or create one manually in the `Efforts/` folder using the effort template.

Efforts live in `Efforts/` when active. When you pause or finish them, move them to `Paused/` or `Completed/`.
## Step 7 — Capture Something

Put something in `+/` — a quick thought, a web clip, a rough note. Don't format it. Don't file it. Just capture.

Later, ask Claude: "Process the inbox" — and watch it file, format, link, and tag your captures.
## Optional — Cowork (Outside Obsidian)

If you want to use Claude outside Obsidian, you can use **Cowork** in the Claude Desktop app. Open Claude Desktop → Cowork tab → select your vault folder. Cowork reads the same configuration as Claudian — same rules, same skills. See [[When to Use What]] for when each is useful.
## Optional — Install the Obsidian Web Clipper

The Obsidian Web Clipper browser extension saves web pages directly into your vault. Install it from your browser's extension store (Chrome, Firefox, Safari, Edge).

After installing, configure it to save clippings to `+/Web/`. Any page you clip lands in your inbox for Claude to process later.
## What's Next

Once you're comfortable with daily notes, inline comments, and captures, you'll naturally discover more patterns. See [[When to Use What]] for ideas on what to ask Claude, and [[IKE Vault Guide]] for the full framework.
## Related Notes

- [[Getting Started Map]]
