---
name: session-log
description: Write the end-of-session log and update project status in the GSP knowledge base. Use at the end of any session that changed something, or when asked to log what happened.
---

# Session log

1. Copy `templates/log.md` to `logs/YYYY-MM-DD-short-topic.md` (today's date, a few lowercase hyphenated words). Fill in every section; write "nothing" under Changed if read-only.
2. Add a row at the top of the table in `logs/README.md`.
3. Update `project/status.md` and its "Last updated" date. Keep its format: newest items at the top; add new work to the top of "To do"; when an item is finished, move it to the top of "Done" as `- [x] YYYY-MM-DD ...` with a link. Never delete checklist items. If dates or phases change, update the Mermaid timeline (keep it valid Mermaid `gantt` syntax).
4. If facts about GSP changed, update the matching file in `client/` or `map/`.
5. If the team made a choice someone might later undo, add a decision in `decisions/` and list it in `decisions/README.md`.
6. Move answered questions out of `project/open-questions.md` into the file where the answer belongs.

Never write plain-text passwords or keys. Never rewrite an old log.
