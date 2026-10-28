# manual-code

A practice repo: small 1–2h exercises the user codes **by hand**. Claude's job is scaffolding, assignments and tests.

## Hard rules
- **Never write or paste the solution** into `problems/` — not as a "reference", not as a hint, unless the user explicitly asks for it. Stubs raise `NotImplementedError` / `todo!()` / `throw new Error('TODO')`.
- To validate generated tests, write a throwaway reference solution in the **session scratchpad**, run it against the tests, then discard it.
- Tests come from the README only, ≥8 cases incl. edge cases, deterministic (inject clocks, seed RNGs, bind sockets to port 0).
- Review feedback on the user's solution = suggestions, not rewrites.

## Layout
- `IDEAS.md` backlog · `LOG.md` finished work · `problems/<ID>-<slug>/README.md` assignment, one subfolder per stack.
- Skills: `/pick-idea`, `/new-problem`, `/add-ideas`, `/finish-problem` (see `.claude/skills/`).
- Templates: `.claude/skills/new-problem/templates/<stack>/` (`__SLUG__`-style placeholders documented in that SKILL.md).

## Known quirk
`cargo` commands at the repo root error ("failed to load manifest … problems/*/rust") until the first rust problem exists; the glob resolves once `/new-problem <ID> rust` has run. Not a bug.

## Running tests
`scripts/t <problem-id> [stack]` picks the right command. One-time install: `scripts/setup`.

| stack | command |
|---|---|
| python | `.venv/bin/pytest problems/<id>/python` |
| node | `node --test problems/<id>/node` |
| go | `go test ./problems/<id>/go/...` |
| rust | `cargo test -p <crate>` (crate name `p_<id>` lowercased, dashes→underscores) |
| web / webcomponent / react | `npx vitest run problems/<id>/<stack>` |
| django | `cd problems/<id>/django && ../../../.venv/bin/python manage.py test` |
