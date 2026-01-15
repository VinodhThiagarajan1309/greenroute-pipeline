# -*- coding: utf-8 -*-
"""pipeline-orchestration: layer naming and per-environment catalog mapping.

Every published table carries a bronze_/silver_/gold_ prefix matching its
layer. Each layer lives in its own Unity Catalog schema; each environment
(dev/staging/prod) is its own catalog.
"""

LAYER_PREFIXES = ("bronze_", "silver_", "gold_")

LAYER_SCHEMAS = {"bronze": "bronze", "silver": "silver", "gold": "gold"}


def layer_of(table_name):
    """Pure: which layer a table name belongs to, from its prefix."""
    for prefix in LAYER_PREFIXES:
        if table_name.startswith(prefix):
            return prefix.rstrip("_")
    raise ValueError("table name %r carries no bronze_/silver_/gold_ prefix" % (table_name,))


def qualified_table_name(catalog, table_name):
    """Pure: <catalog>.<layer-schema>.<table_name>, one catalog per environment."""
    layer = layer_of(table_name)
    return "%s.%s.%s" % (catalog, LAYER_SCHEMAS[layer], table_name)


def bronze_ingest_job_stub(catalog):
    """Job stub: qualified name of the table this bronze job would publish to."""
    return qualified_table_name(catalog, "bronze_payment_events")


def silver_transform_job_stub(catalog):
    """Job stub: qualified name of the table this silver job would publish to."""
    return qualified_table_name(catalog, "silver_payment_events")


def gold_aggregation_job_stub(catalog):
    """Job stub: qualified name of the table this gold job would publish to."""
    return qualified_table_name(catalog, "gold_payment_ledger")
