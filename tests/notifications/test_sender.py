# -*- coding: utf-8 -*-
"""Tests that NotificationSender.send() routes to the registered provider
for the channel.
"""
from greenroute.notifications.sender import NotificationSender, register_provider


def test_send_routes_to_registered_provider_for_channel():
    calls = []

    def fake_provider(recipient, message):
        calls.append((recipient, message))
        return {"ok": True}

    register_provider("test_channel", fake_provider)
    sender = NotificationSender()
    prefs = {("cust-1", "test_channel"): {"opted_in": True}}
    result = sender.send("cust-1", "test_channel", "hi", prefs)
    assert result["sent"] is True
    assert calls == [("cust-1", "hi")]


def test_send_with_no_registered_provider_fails_cleanly():
    sender = NotificationSender()
    prefs = {("cust-2", "carrier_pigeon"): {"opted_in": True}}
    result = sender.send("cust-2", "carrier_pigeon", "hi", prefs)
    assert result["sent"] is False
    assert result["reason"] == "no_provider_registered_for_channel"


def test_send_still_refuses_opted_out_regardless_of_provider():
    register_provider("test_channel_2", lambda r, m: {"ok": True})
    sender = NotificationSender()
    prefs = {("cust-3", "test_channel_2"): {"opted_in": False}}
    result = sender.send("cust-3", "test_channel_2", "hi", prefs)
    assert result["sent"] is False
    assert result["reason"] == "opted_out"
