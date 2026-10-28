---
name: add-ideas
description: Append fresh, non-duplicate practice ideas to IDEAS.md in the established format. Use for "/add-ideas", "more ideas for protocols", "add 10 python scripts ideas".
---

# add-ideas

Arguments (optional): `[category letter or name] [n]` — default 8 ideas across categories that have the fewest unchecked items.

Categories: **A** algorithms & data structures · **B** scripts & CLI · **C** web/JS widgets (incl. wc, react, django) · **D** systems/interview-style · **E** protocols & mini servers (binary parsing, UDP/TLS/TCP). The user may also ask for a new category; use the next free letter and add a `## F — …` heading.

1. Read `IDEAS.md` fully; do not duplicate or near-duplicate existing titles (checked or not).
2. Append each idea to the end of its category in exactly this format, with the next free ID:
   `- [ ] **A20 Title** · ★★ · 1h · py/js/go/rs — one-sentence spec + the key edge case`
3. Ideas must be 30m–2h, self-contained, testable without external services, and not a "full project". Prefer ideas where the interesting part fits in one file. Stack tags: `py js go rs web wc react dj`.
4. Show the user the new lines (not the whole file). Do not scaffold anything.
