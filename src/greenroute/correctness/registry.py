# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""data-correctness: catalog registry of gold tables recon iterates over.

Recon started out hardcoded to gold_schedule_events. It now iterates
whatever the catalog registry lists, so adding parity coverage for a new
gold table is a registry entry, not a new job.
"""
from __future__ import annotations


GOLD_TABLE_REGISTRY = {
    "gold_schedule_events": {
        "key_fields": ["schedule_event_id"],
        "value_fields": ["status", "service_window_start", "technician_id"],
        "timestamp_field": "service_window_start",
        "partition_column": "event_date",
    },
}


def iter_gold_tables(registry=None):
    """Yield (table_name, table_config) for every table recon should check,
    in a stable order.
    """
    registry = GOLD_TABLE_REGISTRY if registry is None else registry
    for table_name in sorted(registry):
        yield table_name, registry[table_name]


GOLD_TABLE_REGISTRY["gold_service_catalog"] = {
    "key_fields": ["service_catalog_id"],
    "value_fields": ["service_name", "zone_tier", "requires_pesticide_license"],
    "timestamp_field": "updated_at",
    "partition_column": "updated_date",
}
