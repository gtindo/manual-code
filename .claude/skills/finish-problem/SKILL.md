---
name: finish-problem
description: Run a problem's tests, tick it off in IDEAS.md, log it in LOG.md and optionally review the user's solution. Use for "/finish-problem A01", "I'm done with the lru cache", "check my solution".
---

# finish-problem

Arguments: `[ID] [stack]` — if omitted, infer from the most recently modified folder under `problems/` (confirm with the user if ambiguous).

1. Run `scripts/t <ID> <stack>`. If tests fail, show the failing test names and the assertion messages only; do **not** fix the user's code or write the solution. Offer a nudge if they want one. Stop here.
2. If green:
   - Tick the idea in `IDEAS.md` (`- [ ]` → `- [x]`). If the idea is already ticked (redo in another stack), leave it.
   - Ask the user how long it took (one short question, optional) and any note.
   - Append one line to `LOG.md`: `YYYY-MM-DD · ID Title · stack · <time> · <note>`.
3. Offer a review (don't force it). If accepted, read the user's solution and give ≤5 concrete suggestions: correctness risks the tests don't cover, complexity, idiom for that stack, readability. Suggestions only — no rewritten solution unless asked. Mention a stretch goal from the README.
4. Suggest the next step: same idea in another stack, or `/pick-idea`.
