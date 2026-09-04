# -*- coding: utf-8 -*-
from datetime import datetime

import pytest

from greenroute.service_catalog.catalog import (
    validate_no_overlapping_active_prices,
    OverlappingActivePrice,
)


def test_overlapping_active_prices_rejected():
    rows = [
        {"service_type_id": "mowing", "zone_tier": "tier_1", "is_active": True,
         "effective_start": datetime(2025, 1, 1), "effective_end": None},
        {"service_type_id": "mowing", "zone_tier": "tier_1", "is_active": True,
         "effective_start": datetime(2025, 6, 1), "effective_end": None},
    ]
    with pytest.raises(OverlappingActivePrice):
        validate_no_overlapping_active_prices(rows)


def test_non_overlapping_sequential_prices_allowed():
    rows = [
        {"service_type_id": "mowing", "zone_tier": "tier_1", "is_active": True,
         "effective_start": datetime(2025, 1, 1), "effective_end": datetime(2025, 5, 31)},
        {"service_type_id": "mowing", "zone_tier": "tier_1", "is_active": True,
         "effective_start": datetime(2025, 6, 1), "effective_end": None},
    ]
    assert validate_no_overlapping_active_prices(rows) == rows


def test_different_tiers_do_not_conflict():
    rows = [
        {"service_type_id": "mowing", "zone_tier": "tier_1", "is_active": True,
         "effective_start": datetime(2025, 1, 1), "effective_end": None},
        {"service_type_id": "mowing", "zone_tier": "tier_2", "is_active": True,
         "effective_start": datetime(2025, 1, 1), "effective_end": None},
    ]
    assert validate_no_overlapping_active_prices(rows) == rows
