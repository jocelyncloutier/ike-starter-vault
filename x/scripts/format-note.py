#!/usr/bin/env python3
"""
format-note.py — Deterministic Obsidian note formatter.

Enforces the vault's Template Conventions from CLAUDE.md:
  1. No blank line after frontmatter
  2. No horizontal rules (---) mid-document
  3. Heading spacing: no blank line before, one blank line after
  4. No blank line before lists
  5. No consecutive blank lines
  6. Trailing newline
  7. Mandatory frontmatter fields: created, authorship, tags

Exit codes: 0 = success, 1 = error.
"""

import argparse
import os
import re
import sys
from datetime import date
from pathlib import Path

FRONTMATTER_FENCE = "---"
HEADING_RE = re.compile(r"^#{2,6}\s")
LIST_RE = re.compile(r"^(\s*[-*+]|\s*\d+[.)]) ")
HR_RE = re.compile(r"^---+\s*$")


def split_frontmatter(lines: list[str]) -> tuple[list[str], list[str]]:
    """Split lines into (frontmatter_lines, body_lines).

    Frontmatter includes the opening and closing --- fences.
    If no valid frontmatter, returns ([], lines).
    """
    if not lines or lines[0].rstrip() != FRONTMATTER_FENCE:
        return [], lines

    for i in range(1, len(lines)):
        if lines[i].rstrip() == FRONTMATTER_FENCE:
            return lines[: i + 1], lines[i + 1 :]

    # Unclosed frontmatter — treat entire content as body
    return [], lines


def is_blank(line: str) -> bool:
    return line.strip() == ""


def is_heading(line: str) -> bool:
    return bool(HEADING_RE.match(line))


def is_list_item(line: str) -> bool:
    return bool(LIST_RE.match(line))



def is_horizontal_rule(line: str) -> bool:
    return bool(HR_RE.match(line))


def format_body(lines: list[str]) -> list[str]:
    """Apply all formatting rules to body lines (after frontmatter)."""
    # --- Pass 1: Remove horizontal rules ---
    lines = [l for l in lines if not is_horizontal_rule(l)]

    # --- Pass 2: Remove blank line immediately after frontmatter ---
    # (body starts right after the closing ---; strip leading blanks)
    while lines and is_blank(lines[0]):
        lines.pop(0)

    if not lines:
        return []

    # --- Pass 3: Apply spacing rules line by line ---
    result: list[str] = []

    for i, line in enumerate(lines):
        stripped = line.rstrip()

        # Look ahead to next non-blank line
        next_content = None
        for j in range(i + 1, len(lines)):
            if not is_blank(lines[j]):
                next_content = lines[j]
                break

        # Current line is blank
        if is_blank(stripped):
            # Rule 5: No consecutive blank lines
            if result and is_blank(result[-1]):
                continue

            # Rule 3: No blank line before headings
            if next_content and is_heading(next_content):
                continue

            # Rule 4: No blank line before lists
            if next_content and is_list_item(next_content):
                # Only remove blank between paragraph text and list.
                # Keep blanks after headings (that's the "one blank after heading" rule).
                if result and not is_blank(result[-1]) and not is_heading(result[-1]):
                    continue

            result.append("")
            continue

        # Current line is a heading
        if is_heading(stripped):
            # Rule 3: No blank line before headings
            if result and is_blank(result[-1]):
                result.pop()

            result.append(stripped)

            # Rule 3: Ensure one blank line after heading
            # (handled by not stripping the next blank, but we need to ensure
            #  there IS one — add it if the next line is non-blank content)
            if next_content is not None:
                # Check if there's already a blank between this heading and next content
                has_blank_after = False
                for j in range(i + 1, len(lines)):
                    if is_blank(lines[j]):
                        has_blank_after = True
                        break
                    else:
                        break
                if not has_blank_after:
                    result.append("")
            continue

        # Regular content line
        result.append(stripped)

    return result


def _file_birth_date(filepath: str | None) -> str:
    """Get the file's birth date as YYYY-MM-DD. Falls back to today."""
    if filepath:
        try:
            stat = os.stat(filepath)
            ts = getattr(stat, "st_birthtime", None) or stat.st_mtime
            return date.fromtimestamp(ts).isoformat()
        except OSError:
            pass
    return date.today().isoformat()


def ensure_frontmatter(fm_lines: list[str], filepath: str | None = None) -> list[str]:
    """Add missing mandatory frontmatter fields (created, authorship, tags).

    Only fills in missing fields — never overwrites existing values.
    If there's no frontmatter at all, returns the lines unchanged.
    """
    if not fm_lines:
        return fm_lines

    # Parse existing fields (between the two --- fences)
    inner = fm_lines[1:-1]
    has_created = any(l.strip().startswith("created:") for l in inner)
    has_authorship = any(l.strip().startswith("authorship:") for l in inner)
    has_tags = any(l.strip().startswith("tags:") for l in inner)

    if has_created and has_authorship and has_tags:
        return fm_lines

    # Build lines to insert before the closing ---
    new_fields: list[str] = []
    if not has_created:
        new_fields.append(f"created: {_file_birth_date(filepath)}")
    if not has_authorship:
        new_fields.append("authorship: human")
    if not has_tags:
        new_fields.append("tags: []")

    return fm_lines[:-1] + new_fields + [fm_lines[-1]]


def format_note(text: str, filepath: str | None = None) -> str:
    """Format a complete note (frontmatter + body)."""
    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = text.split("\n")

    # Remove trailing empty-string from split if file ended with \n
    if lines and lines[-1] == "":
        lines.pop()

    fm_lines, body_lines = split_frontmatter(lines)
    fm_lines = ensure_frontmatter(fm_lines, filepath)
    body_lines = format_body(body_lines)

    # Reassemble
    all_lines = []
    if fm_lines:
        all_lines.extend(l.rstrip() for l in fm_lines)
    all_lines.extend(body_lines)

    # Rule 6: Ensure trailing newline
    return "\n".join(all_lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Format Obsidian notes per vault conventions."
    )
    parser.add_argument(
        "files",
        nargs="+",
        help='Markdown files to format. Use "-" to read from stdin.',
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show diff instead of writing changes.",
    )
    args = parser.parse_args()

    any_changed = False
    any_error = False

    for filepath in args.files:
        try:
            if filepath == "-":
                original = sys.stdin.read()
                formatted = format_note(original)
                if args.dry_run:
                    if original != formatted:
                        _print_diff("<stdin>", original, formatted)
                        any_changed = True
                    else:
                        print("<stdin>: no changes needed")
                else:
                    sys.stdout.write(formatted)
                    if original != formatted:
                        any_changed = True
                continue

            path = Path(filepath)
            if not path.exists():
                print(f"error: {filepath} not found", file=sys.stderr)
                any_error = True
                continue

            original = path.read_text(encoding="utf-8")
            formatted = format_note(original, filepath=str(path))

            if original == formatted:
                if args.dry_run:
                    print(f"{filepath}: no changes needed")
                continue

            any_changed = True
            if args.dry_run:
                _print_diff(filepath, original, formatted)
            else:
                path.write_text(formatted, encoding="utf-8")
                print(f"{filepath}: formatted")

        except Exception as e:
            print(f"error: {filepath}: {e}", file=sys.stderr)
            any_error = True

    if any_error:
        return 1
    return 0


def _print_diff(label: str, original: str, formatted: str) -> None:
    """Print a unified diff between original and formatted."""
    import difflib

    orig_lines = original.splitlines(keepends=True)
    fmt_lines = formatted.splitlines(keepends=True)
    diff = difflib.unified_diff(
        orig_lines, fmt_lines, fromfile=f"a/{label}", tofile=f"b/{label}"
    )
    sys.stdout.writelines(diff)


if __name__ == "__main__":
    sys.exit(main())
