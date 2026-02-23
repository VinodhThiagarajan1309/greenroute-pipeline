# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""data-completeness: gate gold publish on source-window closure.

A gold partition must not publish until every contributing source's
watermark has closed for that window. A blocked publish must say which
source blocked it -- a gate that never fires is indistinguishable from a
gate that was never wired up.
"""
from __future__ import annotations

from datetime import timedelta


class GateResult(object):
    def __init__(self, allowed, blocking_sources, overridden=False, override_reason=None):
        self.allowed = allowed
        self.blocking_sources = blocking_sources
        self.overridden = overridden
        self.override_reason = override_reason

    def __eq__(self, other):
        if not isinstance(other, GateResult):
            return NotImplemented
        return (
            self.allowed == other.allowed
            and self.blocking_sources == other.blocking_sources
            and self.overridden == other.overridden
            and self.override_reason == other.override_reason
        )

    def __repr__(self):
        return "GateResult(allowed={0}, blocking_sources={1}, overridden={2}, override_reason={3!r})".format(
            self.allowed, self.blocking_sources, self.overridden, self.override_reason
        )


def _add_hours(moment, hours):
    return moment + timedelta(hours=hours)


def evaluate_window_closure(source_watermarks, window_end, now, override_reason=None):
    """Evaluate whether a gold partition for `window_end` may publish.

    `source_watermarks` is {source_name: watermark_hours}. A source's
    watermark for this window closes at window_end + watermark_hours. The
    gate opens only once every contributing source has closed.

    `override_reason` is the escape hatch: a human explicitly decided to
    publish early. Overriding is fine; overriding invisibly is not -- callers
    must supply a non-empty reason, and the reason flows through to a
    distinct metric (see emit_gate_metric).
    """
    still_open = []
    for source, watermark_hours in sorted(source_watermarks.items()):
        closes_at = _add_hours(window_end, watermark_hours)
        if now < closes_at:
            still_open.append(source)

    if not still_open:
        return GateResult(allowed=True, blocking_sources=[])

    if override_reason:
        return GateResult(
            allowed=True,
            blocking_sources=still_open,
            overridden=True,
            override_reason=override_reason,
        )

    return GateResult(allowed=False, blocking_sources=still_open)
