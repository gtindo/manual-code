---
name: new-problem
description: Scaffold a practice problem in this repo — assignment README, stub files and failing tests for one or more stacks (python, node, go, rust, web, webcomponent, react, django). Use when the user says "/new-problem A01 python", names an idea from IDEAS.md, or describes a new exercise to set up. Never writes the solution.
---

# new-problem

Arguments: `<idea-id | free text> <stack> [stack…]` — e.g. `A01 python go`, `E03 go`, `"hex dump to ASCII" node`.
If the stack is missing, ask once (suggest the stacks listed on the idea line). If the idea is missing, run the `pick-idea` skill.

## Steps

1. **Resolve the idea.** If it is an ID, read its line in `/home/ytindo/manual-code/IDEAS.md`. If it is free text, invent an entry, give it the next free ID in the best-fitting category, append it to `IDEAS.md`.
2. **Name things.** Folder `problems/<ID>-<slug>/` (slug kebab-case). Placeholders used in templates:
   `__ID__` (A01), `__TITLE__`, `__PKG__` (Go package: slug without dashes), `__CRATE__` (`p_` + folder name lowercased, dashes→underscores, e.g. `p_a01_lru_cache`), `__TAG__` / `__CLASS__` (web component: tag must contain a dash, class PascalCase).
3. **Write `problems/<ID>-<slug>/README.md`** (only if it does not exist yet — the same problem can be redone in another stack). Sections:
   - **Goal** (2–3 sentences) · **Spec** (exact function/CLI/endpoint signatures per stack, behaviour, error cases) · **Examples** (3+ concrete input→output) · **Constraints** (complexity, no stdlib shortcut that defeats the exercise) · **Done when** (test command per stack) · **Stretch** (optional 1–2 extensions).
   - Must be self-contained: the user should not need to read the tests to know what to build. Aim for something doable in the time on the idea line.
4. **Copy the stack template(s)** from `.claude/skills/new-problem/templates/<stack>/` into `problems/<ID>-<slug>/<stack>/`, replacing placeholders. Then adapt:
   - **Stubs:** real signatures from the README, bodies raise `NotImplementedError` / `throw new Error('TODO')` / `panic("TODO")` / `todo!()`. Nothing else implemented.
   - **Tests:** replace the skeleton with ≥8 cases derived from the README only — happy path, each documented error, boundary values, one "bigger" case. Deterministic: inject clocks, seed RNGs, no sleeps. Sockets bind to port `0`; TLS tests read `shared/certs/{cert,key}.pem`.
   - **Fixtures:** shared data goes in `problems/<ID>-<slug>/fixtures/` (hex dumps, `.bin`, sample logs). For protocol problems build bytes by hand from the RFC/spec; note in the README which RFC section is the source.
   - Stack specifics: go → one package per problem under the root module; rust → `Cargo.toml` from template (root workspace picks it up via the `problems/*/rust` glob); react → keep `index.html`, `main.jsx`, `vite.config.js`; django → project is self-contained, tests in `app/tests.py` use `django.test.TestCase`/`Client`.
5. **Prove the tests are red for the right reason.** Run `scripts/t <ID> <stack>`. Failures must come from the stub (NotImplemented / TODO panic), not from import/syntax/config errors. Fix the scaffold until that holds.
6. **Prove the tests are valid.** Write a throwaway reference solution in the **scratchpad directory** (never in `problems/`), copy it temporarily over the stub *in the scratchpad copy of the problem* or run it via a temp copy of the folder, confirm all tests go green, then delete it. If tests contradict the README, fix the tests/README. Confirm the user's repo copy still has stubs only (`git`-less, so re-run `scripts/t` and expect red).
7. **Report briefly:** folder path, the README path to read first, the test command, the time budget. Do not paste the solution or hints beyond the README.

## Rules
- Never leave an implementation in `problems/`. If the user later asks for hints/solution, give the smallest nudge first.
- Don't edit files outside `problems/<ID>-<slug>/` and `IDEAS.md`.
- If a toolchain is missing, tell the user to run `scripts/setup` rather than installing things ad hoc.
