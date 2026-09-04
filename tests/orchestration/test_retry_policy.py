# -*- coding: utf-8 -*-
"""Tests for job-level retry policy (pipeline-orchestration)."""
from greenroute.orchestration.retry_policy import (
    FAILURE_CLASS_FATAL,
    FAILURE_CLASS_RETRYABLE,
    classify_failure,
    retry_plan,
)


def test_gate_failure_is_fatal():
    assert classify_failure("completeness_gate_failed") == FAILURE_CLASS_FATAL
    assert classify_failure("correctness_gate_failed") == FAILURE_CLASS_FATAL


def test_transient_infra_failure_is_retryable():
    assert classify_failure("network_error") == FAILURE_CLASS_RETRYABLE


def test_gate_failure_pages_immediately_no_retry():
    plan = retry_plan("completeness_gate_failed", attempt_number=0)
    assert plan["should_retry"] is False
    assert plan["page_now"] is True


def test_transient_failure_retries_with_backoff():
    plan = retry_plan("network_error", attempt_number=0)
    assert plan["should_retry"] is True
    assert plan["delay_seconds"] > 0


def test_transient_failure_pages_after_max_retries():
    plan = retry_plan("network_error", attempt_number=3)
    assert plan["should_retry"] is False
    assert plan["page_now"] is True
