---
created: 2026-03-10
authorship: ai-generated
tags:
  - type/map
  - topic/ike
---
> First steps after opening this vault. Work through these in order.
## Step 1 — Look Around

You're in Obsidian. The left sidebar (Notebook Navigator) shows your vault's folder structure. The calendar widget at the top lets you create daily notes by clicking a date.

Take a minute to click through the folders: `+/`, `Atlas/`, `Calendar/`, `Efforts/`, `x/`. Each one has a purpose — see [[IKE Vault Guide]] for the full explanation.
## Step 2 — See How Notes Are Structured

Every note in IKE has **frontmatter** — a YAML block at the top that stores metadata like creation date, authorship, and tags. In the default reading view, frontmatter is hidden. Two ways to see it:

- **Source mode** — Click the book/code icon in the top-right of any note to switch between reading and source view. Source mode shows the raw markdown including frontmatter.
- **File Properties panel** — The right sidebar has a "File properties" tab (the `i` icon) that shows the current note's frontmatter in a friendly format. You can edit properties there too.

Click on the sample daily note in `Calendar/2026-03-10.md` and try both views to see how frontmatter looks.
## Step 3 — Edit Your CLAUDE.md

Open `.claude/CLAUDE.md` (you may need to show hidden files — on macOS press Cmd+Shift+. in Finder, or look for the file in Obsidian's file explorer).

Find the **"How You Work"** section. Replace the placeholder prompts with your actual working style: your role, how you capture information, what breaks your systems, your daily tools. This is how Claude learns to help you effectively.
## Step 4 — Open Claude

Open Claude Desktop and start a Cowork session pointed at this vault folder. Claude will read your CLAUDE.md and understand the vault structure.

Try these first conversations:
- "What's in this vault?" — Claude will orient you to the structure
- "Create today's daily note with my meetings" — If you have Google Calendar connected, Claude will pull your schedule
- "Create a note about [something you're thinking about]" — Watch Claude create a properly formatted note with frontmatter and links
## Step 5 — Try the Inline Comment Workflow

Open any note and add a comment like this: `%%rewrite this section to be more concise%%`

Then tell Claude: "Review the comments in [note name]." Claude will find every `%%comment%%`, apply the requested changes, and remove the markers.

This is the core IKE editing pattern — you batch your feedback, then Claude processes it all at once.
## Step 6 — Create Your First Effort

An Effort is a project or piece of work you're actively doing. In Obsidian, create a new note in the `Efforts/` folder using the effort template, or ask Claude: "Create an effort note for [your project]."

Efforts live in the root of `Efforts/` when active. When you pause or finish them, move them to `Paused/` or `Completed/`.
## Step 7 — Capture Something

Put something in `+/` — a quick thought, a web clip, a rough note from a meeting. Don't format it. Don't file it. Just capture.

Later, ask Claude: "Process the inbox" — and watch it file, format, link, and tag your captures.
## Optional — Install the Obsidian Web Clipper

The Obsidian Web Clipper browser extension lets you save web pages directly into your vault. Install it from your browser's extension store (Chrome, Firefox, Safari, Edge).

After installing, configure it to save clippings to `+/Web/` in this vault. This way any article, reference, or page you clip lands in your inbox and Claude can process it later.
## What's Next

Once you're comfortable with daily notes, inline comments, and captures, you'll naturally discover more patterns. See [[When to Use What]] for ideas on what to ask Claude, and [[IKE Vault Guide]] for the full framework.
## Related Notes

- [[IKE Vault Guide]]
- [[When to Use What]]
