# Design: revert-recon-partition-pruning

## Context

See proposal.md for motivation. This change touches `data-correctness`.

## Goals / Non-Goals

**Goals:**

- Reverts the partition-pruning commit from {{PR:correctness-gold-parity-suite}} and adds a guard so an empty-vs-empty comparison can never be reported as a pass again.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Derek Chen:** I filed {{I13}} and I'll say the obvious thing anyway: four days of a
> silent payment ledger check is the number I care about, not the 60% scan reduction we
> gave up. Revert now, retry the optimization when someone can prove the check still
> works under it. Approved.

> **Sofia Alvarez:** The INCONCLUSIVE state is the actual fix. A revert only undoes this
> one predicate; the next one that matches nothing on both sides would have looked exactly
> the same without it. Good that it's a requirement and not a comment in the code.

> **Aisha Bello (async, back from PTO):** Agreed with all of it, and glad someone wrote
> "a check that cannot fail is not a check" back into the spec instead of just fixing the
> column. That's the line from the original recon PR and it's still true - it just turned
> out to apply to a table I hadn't covered with a table-specific test yet.
