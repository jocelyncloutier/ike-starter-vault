---
created: 2026-03-10
authorship: ai-generated
map: ["[[Getting Started Map]]"]
tags:
  - topic/ike
---
> Your orientation to this vault. Start here.
## What Is IKE?

IKE (Integrated Knowledge Environment) is a system where AI does the organizational work that kills most personal knowledge management systems. You capture your thoughts, notes, and ideas. Claude handles the filing, linking, formatting, and synthesis.

Two apps work together: **Obsidian** is where you read, edit, and navigate your notes visually. **Claude** (via Cowork or Claude Code) is where you have conversations that create, update, and connect notes across the vault.
## How the Vault Is Organized

The vault uses the **ACE framework** — five top-level folders that organize by headspace, not by project or role:

- **`+/` (Inbox)** — Where everything lands first. Quick captures go at root. Subfolders sort by source: `Documents/`, `Email/`, `Meetings/`, `Web/`. AI processes items from here into the right locations.
- **`Atlas/` (Knowledge)** — Your permanent knowledge base. Maps of Content live directly in Atlas. `Notes/` holds atomic ideas. `Sources/` holds reference material.
- **`Calendar/` (Time)** — Daily notes live directly in Calendar. One note per day, all meetings in the same note. `Weekly/` and `Monthly/` hold review notes.
- **`Efforts/` (Action)** — Active projects and work live directly in Efforts. Subfolders track intensity: `Later/`, `Paused/`, `Completed/`.
- **`x/` (Extras)** — Templates, attachments, icons, and other infrastructure you rarely touch directly.

This structure is deliberately **role-agnostic**. It survives job changes, career pivots, and shifting interests because it organizes by how you think, not what you're working on right now.
## Maps

Maps are navigation notes that collect links to related notes, sources, and external resources about a topic. They live in `Atlas/` root and are named with a "Map" suffix (e.g., "Product Strategy Map"). They help you see what you know about a topic at a glance, and they help AI quickly understand the context around any subject.

See [[Getting Started Map]] for your orientation to this vault.
## How AI Is Used

The ARC workflow describes how information flows through IKE:

- **Add** — You capture fast and messy. Drop things in `+/`, jot rough meeting notes, paste web clips. Don't worry about formatting or filing.
- **Relate** — Claude links new notes to existing knowledge, adds Maps of Content references, creates connections you might not see.
- **Communicate** — Claude helps you produce outputs from your vault: emails, documents, summaries, decisions, research notes.

See [[When to Use What]] for specific examples of what to ask Claude.
## Key Concepts

- **Folder notes** — Every folder has a note with the same name (e.g., `Atlas/Atlas.md`) that Notebook Navigator uses for icons and display.
- **Frontmatter** — The YAML block at the top of every note. Tracks creation date, authorship, tags, and links to Maps.
- **Inline comments** — Use `%%comments%%` in any note to leave feedback for Claude. Ask Claude to "review the comments in this note" and it will process them all at once.
- **Tags** — `#type/` for what kind of note, `#topic/` for subject matter, `#status/` for workflow state, `#note/` for what needs attention.
## Related Notes

- [[Getting Started Map]]
