# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""Tests for the data-completeness capability: schedule/service-catalog checks."""


def schedule_rows_missing_service_catalog_id(schedule_rows, service_catalog_ids):
    """Completeness check: no schedule row without a corresponding
    service_catalog_id. Returns the offending schedule_event_ids, not a count.
    """
    catalog_ids = set(service_catalog_ids)
    return [
        row["schedule_event_id"]
        for row in schedule_rows
        if row.get("service_catalog_id") not in catalog_ids
    ]


def test_passes_when_every_schedule_row_has_a_service_catalog_id():
    schedule_rows = [
        {"schedule_event_id": "se-1", "service_catalog_id": "svc-mowing"},
        {"schedule_event_id": "se-2", "service_catalog_id": "svc-edging"},
    ]
    catalog_ids = ["svc-mowing", "svc-edging", "svc-mulching"]
    assert schedule_rows_missing_service_catalog_id(schedule_rows, catalog_ids) == []


def test_flags_schedule_row_with_unknown_service_catalog_id():
    schedule_rows = [
        {"schedule_event_id": "se-1", "service_catalog_id": "svc-mowing"},
        {"schedule_event_id": "se-2", "service_catalog_id": "svc-retired"},
    ]
    catalog_ids = ["svc-mowing"]
    assert schedule_rows_missing_service_catalog_id(schedule_rows, catalog_ids) == ["se-2"]


def test_flags_schedule_row_with_missing_service_catalog_id_field():
    schedule_rows = [{"schedule_event_id": "se-1"}]
    catalog_ids = ["svc-mowing"]
    assert schedule_rows_missing_service_catalog_id(schedule_rows, catalog_ids) == ["se-1"]
