# -*- coding: utf-8 -*-
"""
Dispatch helpers for the customer-notifications capability: confirmation
and T-24h reminder sends, wired through the notification_preference
lookup.
"""
from greenroute.notifications.preferences import is_opted_in








# fix: reschedule now checks notification_preference before sending the
# reschedule text -- this is the call-site check pattern that gets
# replaced two commits later because it is exactly the shape of bug that
# let opted-out customers receive reschedule texts in the first place.


# Move confirmation, reminder, cancellation, and reschedule sends onto
# NotificationSender so they share one consent-checked, provider-agnostic
# send path instead of each hand-rolling opted-out checks and provider
# calls.
from greenroute.notifications.sender import DEFAULT_SENDER


def send_confirmation(customer_id, booking, preferences_by_customer_channel, channel="sms"):
    message = "Your GreenRoute booking %s is confirmed." % booking.get("booking_id")
    return DEFAULT_SENDER.send(customer_id, channel, message, preferences_by_customer_channel)


def send_reminder(customer_id, booking, preferences_by_customer_channel, channel="sms"):
    message = "Reminder: your GreenRoute service is scheduled for %s." % booking.get(
        "service_window_start"
    )
    return DEFAULT_SENDER.send(customer_id, channel, message, preferences_by_customer_channel)


def send_cancellation(customer_id, booking, preferences_by_customer_channel, channel="sms"):
    message = "Your GreenRoute booking %s has been cancelled." % booking.get("booking_id")
    return DEFAULT_SENDER.send(customer_id, channel, message, preferences_by_customer_channel)


def send_reschedule(customer_id, booking, preferences_by_customer_channel, channel="sms"):
    message = "Your GreenRoute booking %s has been rescheduled to %s." % (
        booking.get("booking_id"),
        booking.get("service_window_start"),
    )
    return DEFAULT_SENDER.send(customer_id, channel, message, preferences_by_customer_channel)
