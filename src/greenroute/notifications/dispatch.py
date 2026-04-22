# -*- coding: utf-8 -*-
"""
Dispatch helpers for the customer-notifications capability: confirmation
and T-24h reminder sends, wired through the notification_preference
lookup.
"""
from greenroute.notifications.preferences import is_opted_in


def send_confirmation(customer_id, booking, preferences_by_customer_channel, channel="sms"):
    if not is_opted_in(customer_id, channel, preferences_by_customer_channel):
        return {"sent": False, "reason": "opted_out"}
    message = "Your GreenRoute booking %s is confirmed." % booking.get("booking_id")
    return {"sent": True, "reason": "confirmation_sent", "message": message}


def send_reminder(customer_id, booking, preferences_by_customer_channel, channel="sms"):
    if not is_opted_in(customer_id, channel, preferences_by_customer_channel):
        return {"sent": False, "reason": "opted_out"}
    message = "Reminder: your GreenRoute service is scheduled for %s." % booking.get(
        "service_window_start"
    )
    return {"sent": True, "reason": "reminder_sent", "message": message}


def send_cancellation(customer_id, booking, preferences_by_customer_channel, channel="sms"):
    if not is_opted_in(customer_id, channel, preferences_by_customer_channel):
        return {"sent": False, "reason": "opted_out"}
    message = "Your GreenRoute booking %s has been cancelled." % booking.get("booking_id")
    return {"sent": True, "reason": "cancellation_sent", "message": message}
