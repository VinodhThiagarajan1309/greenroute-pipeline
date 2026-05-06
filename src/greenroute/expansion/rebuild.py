# -*- coding: utf-8 -*-
"""
Nightly zone dimension rebuild, replacing the weekly job.

CLOSED, NOT MERGED: this change was closed. The zone dimension rebuild
stayed weekly, which is the reason onboarding a zone still takes about 3
days end to end -- that latency remains an open, unresolved issue at
quarter end. This code is kept as the attempted approach, not as
production behaviour; nothing else in the pipeline calls it.
"""


def compute_nightly_rebuild_schedule(zone_count):
    """Draft schedule for a nightly rebuild, one run per day.

    Never wired up -- see the module docstring.
    """
    return {"cadence": "nightly", "zone_count": zone_count, "runs_per_day": 1}
