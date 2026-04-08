# Design: rename-completeness-to-freshness-guarantees

## Context

See proposal.md for motivation. This change touches `data-completeness`.

## Goals / Non-Goals

**Goals:**

- Proposes renaming the `data-completeness` capability to `data-freshness-guarantees`.

**Non-Goals:**

- Anything not listed in the proposal. If this change grows a second purpose, it is split into two changes rather than widened.

## Decisions

- The approach in the proposal, over the obvious cheaper alternative, for the reason given under *Why*. Recorded here so the next person does not rediscover the trade-off.

## Risks / Trade-offs

> **Aisha Bello:** Completeness and freshness aren't the same property and I don't want to
> lose the distinction. A table can be fresh and incomplete - published on time with a
> whole source missing - and it can be complete and stale - every row present from an
> hour-old batch. The watermark work is about the first. Naming the capability after the
> second describes something we don't actually check.

> **Derek Chen:** Practical cost on top of that: every archived change under
> `data-completeness` keeps its old capability name forever, that's the point of an
> archive. A rename doesn't touch history, it just means the live spec name and every
> reference to it in an archived delta stop matching. And the ODCS contracts going out
> in a few sprints are going to cite the capability by name in `customProperties`. I'd
> rather pick the name once, right before that happens, than twice.

> **Wes Turner:** Also touches every archived delta's spec path if we ever want the two
> to line up again. Small thing each time, not small in total.

> **Sofia Alvarez:** Aisha's distinction is the one that changes my mind, not the churn
> cost - I'd eat the churn for the right name. But if completeness and freshness are
> actually different things, `data-freshness-guarantees` is a worse name for what this
> capability checks, not a better one. Closing this. Leaving the distinction written down
> in design.md so the next person who has this idea finds the answer instead of the
> question.
