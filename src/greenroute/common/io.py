"""Shared Spark I/O helpers for the GreenRoute pipeline.

Every capability reads and writes Unity Catalog tables through this module rather
than calling `spark.table` / `df.write` directly, so that layer naming, catalog
resolution, and quarantine behaviour live in exactly one place.
"""
import os

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# The three medallion layers. A table name is expected to be prefixed with one of
# these plus an underscore, e.g. "bronze_scheduling_events", "silver_service_visit",
# "gold_service_calendar".
LAYERS = ("bronze", "silver", "gold")

_QUARANTINE_TABLE = "bronze_rejected_rows"


def spark_session():
    """Return the active SparkSession, creating one if none exists yet.

    On a Databricks cluster this returns the cluster's shared session; locally it
    builds one from the environment.
    """
    return SparkSession.builder.appName("greenroute").getOrCreate()


def _catalog():
    """The Unity Catalog catalog for the current environment.

    Resolved from the `GREENROUTE_CATALOG` environment variable, which each
    Databricks Asset Bundle target sets to its own catalog (see `databricks.yml`).
    Defaults to the dev catalog so a stray local run can never touch staging or
    prod data.
    """
    return os.environ.get("GREENROUTE_CATALOG", "greenroute_dev")


def _layer_of(table_name):
    for layer in LAYERS:
        if table_name.startswith(layer + "_"):
            return layer
    raise ValueError(
        "table name %r does not start with a known layer prefix %r"
        % (table_name, LAYERS)
    )


def _qualified(table_name):
    layer = _layer_of(table_name)
    return "%s.%s.%s" % (_catalog(), layer, table_name)


def read_table(name):
    """Read a bronze/silver/gold table by its layer-prefixed name.

    `name` must already carry its layer prefix, e.g.
    `read_table("silver_service_visit")`.
    """
    spark = spark_session()
    return spark.table(_qualified(name))


def write_table(df, name, mode="append"):
    """Write `df` to the named table, resolving catalog and schema from its prefix.

    `mode` is passed straight through to the DataFrameWriter ("append",
    "overwrite"); anything needing MERGE semantics does that explicitly and calls
    this only for the final write.
    """
    qualified = _qualified(name)
    (
        df.write.format("delta")
        .mode(mode)
        .option("mergeSchema", "true")
        .saveAsTable(qualified)
    )
    return qualified


def quarantine(df, reason, source):
    """Write rejected rows to the quarantine table instead of dropping them.

    Rejecting is a first-class outcome, never a silent drop: every row in `df` is
    written to `bronze_rejected_rows` tagged with `reason` and `source`, and the
    row count is returned so the caller can emit a metric rather than fail
    silently. Never use `dropna()` or an equivalent filter in place of this.
    """
    tagged = (
        df.withColumn("rejection_reason", F.lit(reason))
        .withColumn("rejection_source", F.lit(source))
        .withColumn("quarantined_at", F.current_timestamp())
    )
    write_table(tagged, _QUARANTINE_TABLE, mode="append")
    return tagged.count()
