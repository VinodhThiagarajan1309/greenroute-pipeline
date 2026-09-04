# -*- coding: utf-8 -*-
"""
routing.zip_lookup: the hardcoded zip -> zone dict that used to live here,
and the CSV in the DAB resources folder, are both deleted. zone_registry
(see greenroute.expansion.zone_registry) is now the single source of
truth for zip -> zone; routing asks zone_registry, never a local dict or
CSV, and -- like every other caller -- only ever needs to ask zone, never
zip, for anything downstream of this lookup.
"""
from greenroute.expansion.zone_registry import zone_for_zip


def zone_for_zip_via_registry(zip_code, registry_by_zip):
    """Routing's zip->zone lookup, delegated entirely to zone_registry."""
    return zone_for_zip(zip_code, registry_by_zip)
