# -*- coding: utf-8 -*-
"""pipeline-orchestration: job-level retry policy.

Retry policy distinguishes a transient infrastructure failure (retry) from
a failed data-quality gate (never retry -- it will fail identically and
retrying only delays the page by however long the backoff takes).
"""

FAILURE_CLASS_RETRYABLE = "retryable"
FAILURE_CLASS_FATAL = "fatal"

TRANSIENT_INFRA_FAILURE_TYPES = frozenset(
    ["cluster_launch_timeout", "network_error", "spot_instance_lost", "cloud_provider_throttled"]
)

GATE_FAILURE_TYPES = frozenset(["completeness_gate_failed", "correctness_gate_failed"])


def classify_failure(failure_type):
    """Pure: retryable vs fatal for one job failure."""
    if failure_type in GATE_FAILURE_TYPES:
        return FAILURE_CLASS_FATAL
    if failure_type in TRANSIENT_INFRA_FAILURE_TYPES:
        return FAILURE_CLASS_RETRYABLE
    return FAILURE_CLASS_FATAL


def evaluate_gate_failure(failure_type):
    """A failed completeness or correctness gate is always fatal -- retrying
    would fail identically and only delay the page by however long the
    retry backoff takes.
    """
    if failure_type not in GATE_FAILURE_TYPES:
        return None
    print("METRIC gate_failure_classified_fatal=1 failure_type=%s" % failure_type)
    return FAILURE_CLASS_FATAL


MAX_RETRIES = 3
BACKOFF_SECONDS = (30, 120, 300)


def retry_plan(failure_type, attempt_number):
    """Pure: given a failure and how many attempts already made, what to do next.

    Returns a dict with should_retry / delay_seconds / page_now.
    """
    failure_class = classify_failure(failure_type)
    if failure_class == FAILURE_CLASS_FATAL:
        return {"should_retry": False, "delay_seconds": 0, "page_now": True}
    if attempt_number >= MAX_RETRIES:
        return {"should_retry": False, "delay_seconds": 0, "page_now": True}
    return {"should_retry": True, "delay_seconds": BACKOFF_SECONDS[attempt_number], "page_now": False}
