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


BLOCKED_METRIC = "completeness.gate.blocked"
OVERRIDDEN_METRIC = "completeness.gate.overridden"


def emit_gate_metric(gate_result, window_end, emit=None):
    """Emit the metric that makes this gate observable.

    A blocked publish emits BLOCKED_METRIC, once per blocking source, so we
    can see how often the gate actually fires and which source is at fault.
    A manual override emits the DISTINCT metric OVERRIDDEN_METRIC, tagged
    with the override reason, so an override is never invisible. `emit` is
    injected so this stays a pure function under test -- it defaults to a
    no-op collector and always returns the events it built.
    """
    events = []

    def _emit(metric_name, tags):
        event = {"metric": metric_name, "tags": tags}
        events.append(event)
        if emit is not None:
            emit(metric_name, tags)

    if gate_result.overridden:
        _emit(
            OVERRIDDEN_METRIC,
            {
                "window_end": str(window_end),
                "blocking_sources": list(gate_result.blocking_sources),
                "reason": gate_result.override_reason,
            },
        )
    elif not gate_result.allowed:
        for source in gate_result.blocking_sources:
            _emit(
                BLOCKED_METRIC,
                {"window_end": str(window_end), "source": source},
            )

    return events
