"""In-process metrics registry for the GreenRoute pipeline.

Pure Python, no Spark, no network: this is what pipeline code calls when it wants
to record that something happened, and what tests call to assert that it did.
Anything that gates or blocks -- a completeness check, a licensing check, a
correctness reconciliation -- is required to emit a metric here when it fires. A
gate that blocks silently is not a gate anyone can audit.

This registry is in-process only; nothing here ships metrics off-box yet. Wiring it
to a real backend is a follow-up, not a blocker for using it today.
"""

_REGISTRY = []


def emit(metric_name, value=1, **tags):
    """Record that `metric_name` fired with `value`, tagged with `**tags`.

    Returns the recorded entry as a dict, mostly so callers and tests can inspect
    it inline without a second lookup.
    """
    entry = {"metric": metric_name, "value": value, "tags": dict(tags)}
    _REGISTRY.append(entry)
    return entry


def all_metrics():
    """Every metric emitted since the last `reset()`, in emission order."""
    return list(_REGISTRY)


def metrics_for(metric_name):
    """Every recorded entry for `metric_name`, in emission order."""
    return [m for m in _REGISTRY if m["metric"] == metric_name]


def was_emitted(metric_name, **tags):
    """Whether `metric_name` fired at least once, optionally matching `**tags`.

    With no tags, this just checks the metric fired at all. With tags, every given
    tag must match an emitted entry's tags exactly.
    """
    for m in metrics_for(metric_name):
        if all(m["tags"].get(k) == v for k, v in tags.items()):
            return True
    return False


def reset():
    """Clear the registry. Called from `tests/conftest.py` between tests."""
    _REGISTRY.clear()
