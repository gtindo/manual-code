# manual-code

## Why this repo exists

The last time I wrote code entirely by hand was in June 2026. Since then I've become convinced that
hand-coding is no longer *necessary* for a software engineer: the tools write it faster, and the job has moved
toward deciding what to build and checking that it's right.

So this repo isn't about necessity. It's for the joy of it: the small satisfaction of reading a problem, thinking
it through, typing it out and watching the tests go green. Like a musician who still plays scales or a runner who
runs with no race coming up, it's a way to stay active and keep the craft in my fingers.

That's why it isn't about end-to-end projects. Every exercise is a small, scoped assignment (30 minutes to 2 hours)
with the boilerplate already done: the folder, the stubs and the failing tests are generated for me, so
the only thing left is the interesting part. I read the assignment, I write the code, and I don't ask anyone else to.

## How it works

Short hand-coded exercises (30m–2h). Read the assignment, code it, make the tests green.

```
scripts/setup          # once: python venv, npm deps, TLS test certs
/pick-idea go 1h       # in Claude Code: get 3 suggestions, pick one → scaffolded for you
/new-problem A01 python go   # or scaffold a specific idea from IDEAS.md in one or more stacks
scripts/t A01 python   # run the tests (red until you solve it)
/finish-problem A01    # tick it off, log it, optional review
/add-ideas protocols 8 # grow the backlog
```

Stacks: python · node · go · rust · web · webcomponent · react · django.
Backlog: [IDEAS.md](IDEAS.md) · History: [LOG.md](LOG.md) · Rules for Claude: [CLAUDE.md](CLAUDE.md).
