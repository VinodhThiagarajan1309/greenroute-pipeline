# -*- coding: utf-8 -*-
"""Tests for the Twilio SMS client wrapper."""
from greenroute.notifications.providers.twilio import (
    send_sms_via_twilio,
    build_twilio_sms_payload,
)


class _FailThenSucceedClient(object):
    def __init__(self, fail_times):
        self.fail_times = fail_times
        self.calls = 0
        self.messages = self

    def create(self, **payload):
        self.calls += 1
        if self.calls <= self.fail_times:
            raise RuntimeError("twilio unavailable")
        return {"sid": "SM123"}


class _AlwaysFailClient(object):
    def __init__(self):
        self.messages = self

    def create(self, **payload):
        raise RuntimeError("twilio unavailable")


def test_build_payload_has_recipient_and_body():
    payload = build_twilio_sms_payload("+15125551234", "hello")
    assert payload["To"] == "+15125551234"
    assert payload["Body"] == "hello"


def test_send_failure_is_retried_once_and_then_succeeds():
    client = _FailThenSucceedClient(fail_times=1)
    result = send_sms_via_twilio("+15125551234", "hello", client=client)
    assert result["ok"] is True
    assert client.calls == 2


def test_send_gives_up_after_max_attempts():
    result = send_sms_via_twilio("+15125551234", "hello", client=_AlwaysFailClient())
    assert result["ok"] is False
    assert result["attempts"] == 2
