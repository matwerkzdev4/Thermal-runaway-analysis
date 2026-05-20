---
name: end-session
description: Create or update a concise SESSION_LOG.md handoff for the current project. Use when the user asks to end a session, log this session, update the session log, prepare context for the next chat, hand off work, or preserve project context before stopping.
---

# End Session

## Purpose

Keep future chats oriented with a short, factual project handoff. Prefer simple English and compact bullets over narrative.

## Workflow

1. Search from the current working directory upward for `SESSION_LOG.md`.
2. If found, append the new session entry there.
3. If not found, create `SESSION_LOG.md` in the project root.
4. Write only useful context for the next chat:
   - Date/time
   - User goal
   - Files inspected or changed
   - Key findings and decisions
   - Current project state
   - Next recommended steps
   - Known caveats or warnings
5. Keep entries concise. Avoid raw command dumps, long chat summaries, duplicate details, and speculation.

## Helper Script

Use `scripts/update_session_log.py` when a deterministic append/create operation is helpful.

Typical use:

```bash
python .codex/skills/end-session/scripts/update_session_log.py --root . --entry path/to/entry.md
```

The entry file should contain the final concise Markdown entry. The script finds an existing `SESSION_LOG.md` by walking upward from `--root`; if none exists, it creates one at `--root/SESSION_LOG.md`.

## Entry Style

Use this compact shape:

```markdown
## YYYY-MM-DD HH:MM - Session Summary

- Goal: ...
- Files: ...
- Findings: ...
- Decisions: ...
- State: ...
- Next: ...
- Caveats: ...
```

If a field has nothing useful, omit it. Do not pad the entry.
