---
created: 2026-03-10
updated: 2026-03-12
authorship: ai-generated
map: ["[[Getting Started Map]]"]
tags:
  - topic/ike
---
> Welcome to your IKE vault. If you're reading this, setup is done — everything is working. This guide helps you get oriented.
## What You Have

This vault is an **IKE (Integrated Knowledge Environment)** — a system where AI handles the organizational work that kills most note-taking systems. You capture fast and messy. Claude files, links, formats, and synthesizes.

**Three tools work together:**

| Tool | What it's for |
|---|---|
| **Obsidian** | Reading notes, editing, navigating the graph, daily notes |
| **Claudian** (right sidebar) | Talking to Claude — creating notes, processing captures, research, drafting |
| **Cowork** (Claude Desktop) | Using Claude outside Obsidian — research, brainstorming, multi-app work |
## Meet Claudian

The **Claudian** tab in the right sidebar is your AI assistant. Try these first conversations:
- **"What's in this vault?"** — Claude orients you to the structure
- **"Create today's daily note"** — creates a formatted daily note
- **"Create a note about [something you're thinking about]"** — Claude creates a note with the right structure and links

![[Vault-start-state.png]]

Claude already knows your vault's folder structure, templates, and conventions. Over time, you can teach it about your role, tools, and preferences by editing `.claude/CLAUDE.md` — but that's optional and not needed now.
## Your Vault Structure

The left sidebar (Notebook Navigator) shows five folders. Click through them:
- **`+/` (Inbox)** — Everything lands here first. Don't organize — just capture.
- **`Atlas/` (Knowledge)** — Your permanent knowledge base. Maps of Content, notes, and references.
- **`Calendar/` (Time)** — Daily notes, weekly and monthly reviews. Click a date in the calendar widget to create a daily note.
- **`Efforts/` (Action)** — Active projects and work. Subfolders: `Later/`, `Paused/`, `Completed/`.
- **`x/` (Extras)** — Templates, attachments, infrastructure. You rarely touch this directly.

This structure is deliberately **role-agnostic** — it survives job changes and shifting interests because it organizes by how you think, not what you're working on. See [[IKE Vault Guide]] for the full explanation.
## Try These Next
### Create an Effort

An Effort is a project or piece of work you're actively doing. Try it now — tell Claude: **"Create an effort note about learning to use Obsidian and IKE."** You can always delete it later.

Efforts live in `Efforts/` when active. When you pause or finish them, move them to `Paused/` or `Completed/`.
### Capture Something

Try it now: create a new note in `+/` and type a quick thought — maybe something you want to learn this week, or an idea you've been sitting on. Don't format it. Don't file it. Just capture.

Later, tell Claude: **"Process the inbox"** — and watch it file, format, link, and tag your captures automatically.
## Optional
### Obsidian Web Clipper

Not required, but one of the best ways to grow your vault. The [Obsidian Web Clipper](https://obsidian.md/clipper) browser extension saves web pages directly into your vault (Chrome, Firefox, Safari, Edge). Configure it to save clippings to `+/Web/`. Any article, reference, or resource you clip lands in your inbox — and Claude can process, summarize, and link it to your existing knowledge later.
## Learn More

- [[When to Use What]] — what to ask Claude
- [[IKE Vault Guide]] — how the vault is organized and why
