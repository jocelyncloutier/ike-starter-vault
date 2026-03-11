---
created: 2026-03-10
authorship: ai-generated
tags:
  - topic/ike
---
## Context

A guide to how Efforts work in IKE. You can delete this note once you're comfortable with the flow.
## An Effort Is a Project or Body of Work

Anything you're actively working on gets an Effort note: a project at work, a home renovation, learning a new skill, planning a trip, writing a document. If it takes more than one sitting and you need to track progress, it's an Effort.
## Folder = Status

The folder an Effort sits in tells you its status — no tags or properties needed:

- **`Efforts/`** (root) — Active. You're working on this now.
- **`Efforts/Later/`** — Queued. You'll get to it, but not right now.
- **`Efforts/Paused/`** — On hold. Something is blocking it or priorities shifted.
- **`Efforts/Completed/`** — Done. Kept for reference.

Move notes between folders as their status changes. That's the only "management" required.
## What an Effort Note Contains

A typical Effort note has:

- **What** — One sentence describing the effort.
- **Why** — Why it matters. What outcome you're after.
- **Current Status** — Where things stand right now.
- **Key Notes** — Links to related notes across the vault (meeting notes, research, decisions).
- **Next Actions** — Tasks to do next, as checkboxes.
- **Changelog** — A running log of what happened and when.
## Working on an Effort

The core pattern: open Claude, say "Let's keep working on [Effort name]." Claude reads the note, reviews any `%%inline comments%%` you've left since the last session, checks related notes for new context, and picks up where you left off.

Leave `%%comments%%` in the Effort note between sessions — "this section needs rewriting," "check if the deadline changed," "add the decision from Friday's meeting." Claude processes them all on the next session.
## Creating an Effort

Create a new note in `Efforts/` using the effort template (Templater will apply it automatically), or ask Claude: "Create an effort note for [your project]."
