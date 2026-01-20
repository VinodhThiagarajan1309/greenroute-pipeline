# -*- coding: utf-8 -*-
import pytest

from greenroute.service_catalog.catalog import resolve_service_type, UnknownServiceType


def test_resolve_active_service_type():
    catalog = [
        {"service_type_id": "mowing", "is_active": True},
        {"service_type_id": "mowing", "is_active": False},
    ]
    row = resolve_service_type(catalog, "mowing")
    assert row["is_active"] is True


def test_unknown_service_type_is_not_defaulted():
    catalog = [{"service_type_id": "mowing", "is_active": True}]
    with pytest.raises(UnknownServiceType):
        resolve_service_type(catalog, "power_washing")


def test_duplicate_active_rows_raise():
    catalog = [
        {"service_type_id": "mowing", "is_active": True},
        {"service_type_id": "mowing", "is_active": True},
    ]
    with pytest.raises(ValueError):
        resolve_service_type(catalog, "mowing")
