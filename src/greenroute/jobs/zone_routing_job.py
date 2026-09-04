# -*- coding: utf-8 -*-
"""pipeline-orchestration: job entry point for zone routing.

Zone grouping and stop ordering logic now lives in scheduling
(src/greenroute/scheduling/routing.py) -- this job is a thin wrapper that
delegates to it. It no longer accepts a routing-strategy parameter from
the DAB job config.
"""


def run_zone_routing_job(spark, catalog, target_date):
    """Spark entry point: read today's bookings, delegate routing to scheduling."""
    from greenroute.common import read_table, write_table
    from greenroute.scheduling.routing import group_by_zone_and_order_stops

    bookings_df = read_table(spark, "silver_bookings").filter("service_date = '%s'" % target_date)
    bookings = [r.asDict() for r in bookings_df.collect()]
    routed = group_by_zone_and_order_stops(bookings)
    write_table(spark.createDataFrame(routed), "silver_routed_stops", mode="overwrite")
    return routed


def validate_zone_routing_job_params(params):
    """wip: port of the drive-time fix from the closed zone-routing PR.

    The job no longer accepts a routing_strategy override -- that knob is
    gone now that scheduling owns zone grouping and stop ordering. This
    guards against a stale bundle config still passing one.
    """
    if "routing_strategy" in params:
        raise ValueError(
            "routing_strategy is no longer a valid job parameter; "
            "zone grouping and stop ordering are owned by scheduling now"
        )
    return params
