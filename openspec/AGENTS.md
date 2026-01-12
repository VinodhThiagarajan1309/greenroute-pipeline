# Conventions for proposing a change

Read this before opening `openspec/changes/<change-id>/`, whether you are a new engineer
or an agent. OpenSpec generates the slash commands under `.claude/commands/opsx/`; this
file is the house style layered on top of them.

## The loop

`/opsx:explore` -> `/opsx:propose <change-id>` -> `/opsx:apply` -> `/opsx:update` (if the
plan changes) -> `/opsx:sync` -> `/opsx:archive`. Explore first. Proposals written without
reading the code describe a plausible system rather than the actual one.

## Where a change lives

    openspec/changes/<change-id>/
      proposal.md                    what should change, and why
      tasks.md                       the checklist -- every box ticked before archive
      design.md                      (optional) a decision with real alternatives
      specs/<capability>/spec.md     one DELTA per capability this change touches

## A delta records the DIFFERENCE, not the whole capability

A delta groups its requirements under exactly these section headings:

    ## ADDED Requirements       brand-new behaviour
    ## MODIFIED Requirements    existing behaviour that changes -- restate it in full
    ## REMOVED Requirements     behaviour going away, with one line on why

Inside each section:

    ### Requirement: <name>
    The system SHALL <one observable behaviour>.

    #### Scenario: <case name>
    - **WHEN** <the condition>
    - **THEN** <the observable outcome>

`openspec validate --all` enforces this. A spec without `## Purpose` and `## Requirements`,
or a scenario not written as **WHEN**/**THEN** bullets, fails and reports zero requirements.

On `/opsx:sync` the deltas are folded into the permanent file
`openspec/specs/<capability>/spec.md`; a REMOVED requirement is deleted from it. That file
is always current. An archived delta is a historical record of one step.

## What makes a good requirement

One behaviour, one SHALL, stated so plainly you could hand it to someone else to test.
Behaviour, never implementation: "retries use exponential backoff with a 3-attempt cap"
is a requirement; "retries use a while loop in retry.py" is a design note.

**The colleague test:** could a colleague who has never opened the code read this and tell
you whether the system satisfies it? If the answer depends on reading the implementation,
the requirement is not finished.

## Brownfield rule

Write specs only for the slice you are changing. Do not back-fill specs for code nobody is
touching -- nothing forces them to track reality, and they go stale.
