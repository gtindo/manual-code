---
name: pick-idea
description: Suggest 3 unchecked ideas from IDEAS.md that fit a stack and time budget, let the user choose, then scaffold it with new-problem. Use for "/pick-idea", "what should I code today", "give me something for 1h in go".
---

# pick-idea

Arguments (all optional): `[stack] [time]` — e.g. `go 1h`, `python`, `45m`.

1. Read `/home/ytindo/manual-code/IDEAS.md` and `/home/ytindo/manual-code/LOG.md`. Keep only unchecked `- [ ]` ideas whose stack list includes the requested stack and whose time is ≤ the budget (if given).
2. Prefer variety: pick 3 ideas from different categories, and avoid categories the user did last (see LOG.md).
3. Present them via AskUserQuestion: label = `ID Title`, description = difficulty, time and the one-line spec. Include the stack choice as a second question only if the user didn't give a stack.
4. On selection, invoke the `new-problem` skill with the chosen ID and stack(s).
5. If fewer than 3 match, say so and offer to run `add-ideas`.
