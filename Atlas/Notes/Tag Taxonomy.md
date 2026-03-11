---
created: 2026-03-10
authorship: ai-generated
map: ["[[IKE Vault Guide]]"]
tags:
  - topic/vault-structure
---
## Context

Defines every tag used in the vault. AI agents should consult this before applying tags. Referenced by CLAUDE.md as the canonical tag reference.
## Type Tags — What Kind of Note Is This?

Applied once per note, usually by template.

| Tag | Meaning | Applied By |
|---|---|---|
| `#type/daily` | Daily note | Template (auto) |
| `#type/weekly` | Weekly review | Template (auto) |
| `#type/monthly` | Monthly review | Template (auto) |
| `#type/map` | Map of Content | Template (manual) |
| `#type/effort` | Project or effort note | Template (manual) |
| `#type/source` | Reference material (book, article, etc.) | Template (manual) |
## Topic Tags — What Subject Does This Cover?

Open-ended. Format: `#topic/[subject]` — lowercase, hyphenated for multi-word.

Examples: `#topic/product-management`, `#topic/obsidian`, `#topic/ai-integration`

Guidance: Be specific enough to be useful but general enough to reuse. If you'd search for it later, it's a good topic tag.
## Status Tags — Where Is This in Its Lifecycle?

Used by AI during ARC workflow automation. **NOT used on effort notes** — the folder (Active/Later/Paused/Completed) is the status.

| Tag | Meaning | Typical Transition |
|---|---|---|
| `#status/inbox` | Raw capture, unprocessed | Applied on capture, removed after processing |
| `#status/review` | Needs human review | Applied by AI when staging content |
## Workflow Tags — What Does This Note Need?

| Tag | Meaning | Action Needed |
|---|---|---|
| `#note/boat🚤` | Orphan note — no other notes link to it | Find related notes and add links |
| `#note/develop🌿` | Has connections but needs more work | Expand, clarify, refine, or cite |
