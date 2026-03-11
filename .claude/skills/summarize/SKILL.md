---
name: summarize
description: Summarize a note and insert a collapsible AI Summary callout after the frontmatter. Use when the user wants to generate or refresh a summary for any note.
---

Summarize a note and insert a collapsible AI Summary callout after the frontmatter.

Arguments: `<note-path>`
- The path to the note to summarize, relative to the vault root
- Example: `summarize Efforts/My Project.md`

$ARGUMENTS

## Steps

1. Read the note at the given path.
2. If the note already contains a `> [!abstract]- AI Summary` callout, remove the entire callout block (all consecutive lines starting with `>` after the callout header) before proceeding.
3. Summarize the note content (excluding any previous AI Summary):
   - Write 3–6 sentences of overview, then 2–5 key bullet points.
   - Use **bold** for emphasis on key concepts.
   - Be concise — capture the core argument and actionable takeaways.
   - End with a **Key takeaway:** one-liner if appropriate.
   - Do NOT use headings inside the summary.
4. Re-read `.claude/CLAUDE.md` Template Conventions before inserting. Insert the summary immediately after the frontmatter closing `---` as a collapsed Obsidian callout. **No blank line** between the callout and the next element:

```
---
> [!abstract]- AI Summary
> [summary content here, each line prefixed with > ]
## Next Heading
```

5. Add `ai-summarized` to the note's `tags` list in frontmatter (if not already present).
