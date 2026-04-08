# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""Tests for parity checks across the gold table registry."""
from greenroute.correctness.recon import compare_rows
from greenroute.correctness.registry import GOLD_TABLE_REGISTRY


def test_seeded_mismatch_is_detected_on_gold_payment_ledger():
    config = GOLD_TABLE_REGISTRY["gold_payment_ledger"]
    incremental_rows = [
        {"payment_id": "pay-1", "amount_cents": 4500, "provider_event_id": "evt-1", "settlement_status": "settled"},
    ]
    # Seed a mismatch: batch recompute disagrees on the settled amount.
    batch_rows = [
        {"payment_id": "pay-1", "amount_cents": 4600, "provider_event_id": "evt-1", "settlement_status": "settled"},
    ]

    mismatches = compare_rows(incremental_rows, batch_rows, config["key_fields"], config["value_fields"])

    assert len(mismatches) == 1
    assert mismatches[0]["diffs"]["amount_cents"] == {"incremental": 4500, "batch": 4600}


def test_seeded_mismatch_is_detected_on_gold_service_catalog():
    config = GOLD_TABLE_REGISTRY["gold_service_catalog"]
    incremental_rows = [
        {
            "service_catalog_id": "svc-pesticide",
            "service_name": "Pesticide application",
            "zone_tier": "premium",
            "requires_pesticide_license": True,
        },
    ]
    # Seed a mismatch: batch recompute disagrees on the license requirement.
    batch_rows = [
        {
            "service_catalog_id": "svc-pesticide",
            "service_name": "Pesticide application",
            "zone_tier": "premium",
            "requires_pesticide_license": False,
        },
    ]

    mismatches = compare_rows(incremental_rows, batch_rows, config["key_fields"], config["value_fields"])

    assert len(mismatches) == 1
    assert mismatches[0]["diffs"]["requires_pesticide_license"] == {"incremental": True, "batch": False}
