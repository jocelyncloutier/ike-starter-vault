# IKE Starter Vault — Claude Context

## What This Is

An **IKE (Integrated Knowledge Environment)** vault — an AI-native personal knowledge management system built on Obsidian. IKE uses Nick Milo's ACE folder framework and LYT (Linking Your Thinking) methodology, with AI handling the organizational work that kills most PKM systems.

Ideas flow through the **ARC workflow**: **Add** (capture to inbox) → **Relate** (AI links to maps and other notes) → **Communicate** (produce outputs — emails, documents, summaries, decisions).

Two apps, clear roles:

| App | Role |
|---|---|
| **Claude** (Cowork or Claude Code) | AI interaction — conversations, processing, synthesis |
| **Obsidian** | Visual editing — read notes, edit notes, navigate the graph, daily notes |

## Folder Structure (ACE)

Obsidian sorts alphabetically. `+` sorts before A-Z.

| Folder | Headspace | Purpose |
|---|---|---|
| `+/` | **Add** (Inbox) | Quick captures at root. Subfolders: Documents/, Email/, Meetings/, Web/ |
| `Atlas/` | **Knowledge** | Maps of Content live here directly. Subfolders: Notes/, Sources/ |
| `Calendar/` | **Time** | Daily notes live here directly. Subfolders: Weekly/, Monthly/ |
| `Efforts/` | **Action** | Active efforts live here directly. Subfolders: Later/, Paused/, Completed/ |
| `x/` | **Extras** | Templates, attachments, icons, utilities |

### Subfolders

- `Atlas/Notes/` — Atomic notes (one idea per note)
- `Atlas/Sources/` — Reference material (books, articles, people, research)
- `Calendar/Weekly/` — Weekly reviews
- `Calendar/Monthly/` — Monthly reviews
- `Efforts/Later/` — Will do, not now
- `Efforts/Paused/` — On hold, might come back
- `Efforts/Completed/` — Done
- `x/Attachments/` — All non-markdown files embedded in notes (images, screenshots, PDFs-as-attachments). This is the Obsidian attachment folder setting.
- `x/Templates/` — Note templates

## How You Work

> **Edit this section.** Claude reads it at the start of every session to understand your working style. Replace the prompts below with your actual habits. The more specific you are, the better Claude can help.

- **Your role:** What do you do? (e.g., product manager, researcher, student, writer)
- **How you capture information:** Do you capture fast and messy, or structured and deliberate?
- **What breaks your systems:** What has killed your past organizational systems? (maintenance burden, context switches, too many categories, etc.)
- **Your daily tools:** What apps and services do you use daily? (email provider, calendar, document tools, messaging)
- **Your communication style:** Do you prefer direct and concise, or detailed and thorough?

## AI Rules — MUST FOLLOW

### 1. Frontmatter Tracks Authorship

The `authorship` property (`ai-generated`, `ai-assisted`, `human`) on every note is sufficient to distinguish AI-created content. AI may write directly to any folder — no staging area required.

### 2. Always Include Frontmatter

Minimum required:
```yaml
---
created: YYYY-MM-DD
authorship: ai-generated
tags: []
---
```

Add `map: ["[[Map Name]]"]` only for notes in `Atlas/Notes/` or `Atlas/Sources/` where a conceptual Map of Content link is meaningful.

### 3. Set Authorship Correctly

- `authorship: ai-generated` — Content created by AI
- `authorship: ai-assisted` — Editing existing human content

### 4. Always Include Context Section

Add `## Context` section explaining why the note was created.

### 5. Link to Existing Notes

Check `Atlas/` first for relevant Maps of Content. Link to existing notes using `[[wikilinks]]`.

### 6. Append Changelog When Updating

When updating existing notes, append changelog entry at bottom:
```markdown
---
## Changelog
- YYYY-MM-DD: [description of change] (ai-assisted)
```

### 7. Never Delete Notes

To deprecate, set `confidence: stale` in frontmatter. Never delete.

### 8. Don't Reorganize Around Current Role

The vault structure is deliberately role-agnostic. Never reorganize folders or categories around current projects, teams, or roles. ACE survives career transitions by design.

### 9. Never Create Maintenance Burden

Don't suggest workflows that require regular human review, manual tagging, or inbox processing rituals. If something needs maintaining, it's Claude's job.

### 10. Surface Action Items Early

In AI-generated docs, place action items, next steps, and immediate tasks near the top of the document (after context/problem statement, before deep reference material). Users scan docs quickly — actionable items must not be buried at the bottom.

### 11. Images and Media Go to `x/Attachments/`

When converting documents or saving web content that includes images, extract images to `x/Attachments/` and reference them from there. Never create `attachments/`, `images/`, or `media/` subfolders next to notes.

## Frontmatter Schema

### Minimal (Required)

```yaml
---
created: YYYY-MM-DD
authorship: human | ai-assisted | ai-generated
tags: []
---
```

### Optional Fields

```yaml
---
map: ["[[Map of Content]]"]    # list — links to Maps of Content (Atlas/Notes/ and Atlas/Sources/ only)
related: ["[[Note A]]", "[[Note B]]"]
in: "[[Category]]"
updated: YYYY-MM-DD
rank: 1
confidence: high | medium | low | stale
source: personal | research | capture | ai-synthesis
capture-from: email | web | meeting | document | manual
review-due: YYYY-MM-DD
effort: "[[Effort Name]]"
icon: icon-name                # Notebook Navigator display icon (folder notes)
---
```

### The `map` Property — How to Set It

`map` links a note to its conceptual Map(s) of Content. It is a **list** (a note can belong to multiple maps) and is **optional**.

| Note location | `map` guidance |
|---|---|
| `Atlas/Notes/` | Set to the relevant Map(s) of Content, e.g. `map: ["[[Software Architecture]]"]` |
| `Atlas/Sources/` | Set to the relevant Map(s) of Content |
| Daily notes, weekly/monthly reviews | Do not include `map` — folder location is sufficient |
| Effort notes | Do not include `map` — folder location is sufficient |
| Map notes (`Atlas/`) | Do not include `map` — a map doesn't need to point to itself |
| All other notes | Optional — include only if the note has a meaningful conceptual parent map |

**Rule:** `map` = which Map of Content does this note belong to? Only set it when folder location alone doesn't tell you the note's topic family.

## Template Conventions

- No `#` heading in note body — the filename is the title. Start at `##`.
- **No blank line after frontmatter.** The first content line (heading, callout, etc.) goes immediately after the closing `---`.
- **No horizontal rules (`---`) between sections.** Headings provide enough visual separation. Reserve `---` for the frontmatter delimiters only.
- **Heading spacing:** No empty line before headings, one empty line after. Applies to all levels (`##` through `######`). Headings have built-in top margin in Obsidian.
- **No blank line before lists.** When a paragraph is followed by a bullet or numbered list, the list starts on the next line with no blank line separating them.
- **No consecutive blank lines.** One blank line max between any elements.
- Templates live in `x/Templates/`.
- Uses Templater plugin (not core Templates).

## Folder Notes and Icons

Every ACE folder has a **folder note** — a markdown file with the same name as its parent directory (e.g., `Atlas/Atlas.md`). Each folder note includes an `icon` frontmatter property that Notebook Navigator uses for display.

| Folder | Icon |
|---|---|
| `+/` | inbox |
| `+/Documents/` | files |
| `+/Email/` | mail |
| `+/Meetings/` | users |
| `+/Web/` | globe-2 |
| `Atlas/` | globe |
| `Atlas/Notes/` | file-text |
| `Atlas/Sources/` | library |
| `Calendar/` | calendar |
| `Calendar/Weekly/` | calendar |
| `Calendar/Monthly/` | calendar |
| `Efforts/` | hammer |
| `Efforts/Later/` | hammer |
| `Efforts/Paused/` | hammer |
| `Efforts/Completed/` | hammer |
| `x/` | box |
| `x/Templates/` | stamp |
| `x/icons/` | pen-tool |

Icons come from Phosphor Icons (bundled in Notebook Navigator). When creating new folders, always create a matching folder note with an appropriate `icon` property.

## Tags

### Type Tags — What Kind of Note Is This?

Applied once per note, usually by template.

| Tag | Meaning |
|---|---|
| `#type/daily` | Daily note |
| `#type/weekly` | Weekly review |
| `#type/monthly` | Monthly review |
| `#type/map` | Map of Content |
| `#type/effort` | Project or effort note |
| `#type/source` | Reference material |

### Topic Tags

Open-ended. Format: `#topic/[subject]` — lowercase, hyphenated for multi-word. Examples: `#topic/product-management`, `#topic/ai-integration`, `#topic/obsidian`.

### Status Tags

Used by AI during ARC workflow automation. **NOT used on effort notes** — the folder (Active/Later/Paused/Completed) is the status.

| Tag | Meaning |
|---|---|
| `#status/inbox` | Raw capture, unprocessed |
| `#status/review` | Needs human review |

### Workflow Tags

| Tag | Meaning |
|---|---|
| `#note/boat🚤` | Orphan note — no other notes link to it |
| `#note/develop🌿` | Has connections but needs more work |

## Daily Note Structure

Daily notes use this structure. There is one note per day. All meetings go in the same note, not separate notes per meeting.

```
## Today's Focus
## Meeting Notes
### [time — meeting name]
```

When creating a daily note from a calendar, each meeting becomes a `###` heading with time, attendees, and meeting link — all pre-populated in one note, ready for note-taking.

## Inline Comment Workflow

A key IKE interaction pattern. You leave `%%comments%%` throughout a note — corrections, questions, rewrite instructions, structural feedback — then ask Claude to process them all at once.

When asked to review comments in a note:
1. Scan the entire note for `%%...%%` comments
2. Interpret each comment in context of the surrounding text
3. Apply the requested change directly — rewrite, reframe, add content, fix formatting
4. When a comment is ambiguous or requires a judgment call, ask for clarification before changing
5. Remove the `%%...%%` markers once addressed
6. If a comment has implications for other notes (e.g., "the one-pager needs different framing"), leave a visible callout or note in the doc rather than silently propagating changes

## AI Responsibilities

Beyond following the rules above, Claude should proactively:

1. **Surface connections.** When working on any note, look for related content across the vault — especially meeting notes that connect to efforts, and decisions that connect to earlier discussions.
2. **Be a thinking partner.** When the user is writing or deciding, pull relevant context from across the vault. Don't just answer questions — synthesize what's already in the vault with what's being discussed.
3. **Never create maintenance burden.** Don't suggest workflows that require regular human review, manual tagging sessions, or inbox processing rituals. If something needs maintaining, it's Claude's job.
4. **When in doubt about where something goes, put it in `+/`** rather than asking.

## Interaction Preferences

- Be direct. Skip preamble and caveats.
- Always use `[[wikilinks]]` for internal links, never markdown-style links.
- **"Clean up" = reformat in place, nothing more.** When asked to clean up a note, only fix formatting (broken lists, whitespace, typos, structure). Do not move, refile, relink, update other notes, or rewrite content. If additional actions seem worthwhile, suggest them separately and wait for approval.
- Accuracy matters more than speed.
- Verify Obsidian features before suggesting them — don't recommend features that don't exist.

## Note Creation & Review Process

When creating, formatting, or reviewing any note:

1. **Re-read** the Frontmatter Schema and Template Conventions sections of this file before proceeding. Do not work from memory.
2. **Verify** each rule against the actual file content, line by line.
3. **When reviewing**, report only issues you can tie to a specific rule in this file and a specific line number in the note. If you can't point to both, don't flag it.

## Shared Memory

Claude's memory file is `.claude/memory/MEMORY.md` inside this vault. At the start of each session, read it for persistent context. Update it when new stable patterns are confirmed — tool paths, recurring preferences, conventions that have evolved past what CLAUDE.md covers.
