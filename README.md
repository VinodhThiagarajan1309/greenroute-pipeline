# GreenRoute Pipeline

GreenRoute is a lawn-care company operating across roughly 40 neighborhoods in and
around Austin, TX — Zilker, Mueller, Circle C, Round Rock, Pflugerville, and more.
We sell mowing, edging, mulching, fertilization, pesticide application, and leaf
cleanup, dispatched by zone and technician.

This repo is the Databricks pipeline that turns raw booking, scheduling and payment
events into the tables the business runs on.

## Medallion layout

Three layers, one Unity Catalog schema per layer, one catalog per environment
(`greenroute_dev`, `greenroute_staging`, `greenroute_prod`):

- `bronze_<source>` — raw events landed as-is from a source system, e.g.
  `bronze_scheduling_events`.
- `silver_<entity>` — cleaned, deduplicated, one row per real-world entity, e.g.
  `silver_service_visit`.
- `gold_<business_concept>` — a business concept, never a source system name, e.g.
  `gold_service_calendar` rather than `gold_scheduling_events`. This is what
  dispatch and finance query directly.

A table's prefix is not decoration — `src/greenroute/common/io.py` uses it to
resolve which catalog schema the table lives in.

## Repo layout

```
openspec/            capability specs and the change proposals that produced them
src/greenroute/      pipeline code, one package per capability
  common/            shared Spark and metrics helpers — import these, don't redefine them
tests/                pytest suite; pure-function tests only, no SparkSession in CI
databricks.yml        Databricks Asset Bundle (dev / staging / prod)
```

Anything that changes system behaviour goes through OpenSpec first: propose, write
the delta spec, review, merge, archive. See `openspec/AGENTS.md` before opening a
change.

## Running tests

```
pip install -e ".[dev]"
pytest
```

Tests only exercise pure functions for now — no SparkSession fixture. We're two
people in week one and we'd rather keep CI under a minute than have full coverage
of code that doesn't exist yet.

---

## About this repository

This is a **synthetic repository**, generated in a single session to illustrate what a
quarter of OpenSpec practice looks like as it accumulates.

GreenRoute is not a real company. The eight engineers named in the commit history are
fictional, and their email addresses use `greenroute.example.com` - a domain reserved by
RFC 2606 precisely so it can never belong to anyone. The commit dates are backdated; the
pull requests and issues are real GitHub objects created in chronological order, so their
numbering follows the story even though GitHub stamps their creation time with the day the
repository was built.

What is genuine: the code parses and the test suite passes, the OpenSpec artifacts follow
the real grammar, and every requirement in `openspec/specs/` traces back to an archived
change under `openspec/changes/archive/` that introduced it.

Please don't cite it as evidence of anything except what a populated OpenSpec repository
looks like from the outside.
