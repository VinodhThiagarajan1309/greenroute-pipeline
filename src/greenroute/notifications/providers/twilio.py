# -*- coding: utf-8 -*-
"""
Twilio client wrapper for the customer-notifications capability's SMS
channel: builds Messages API payloads and sends them, with one retry on
failure.
"""


def build_twilio_sms_payload(recipient, message, from_number="+15125550100"):
    """Pure: build the Twilio Messages API request payload."""
    return {"To": recipient, "From": from_number, "Body": message}


def send_sms_via_twilio(recipient, message, client=None, max_attempts=2):
    """Send one SMS via Twilio's Messages API, retrying once on failure.

    `client` is injected (a Twilio REST client or a test double) so this
    stays testable without real network calls; it must expose
    `.messages.create(**payload)` and raise on failure.
    """
    payload = build_twilio_sms_payload(recipient, message)
    last_error = None
    for attempt in range(1, max_attempts + 1):
        try:
            client.messages.create(**payload)
            return {"ok": True, "attempts": attempt}
        except Exception as exc:
            last_error = exc
    return {"ok": False, "attempts": max_attempts, "error": str(last_error)}
