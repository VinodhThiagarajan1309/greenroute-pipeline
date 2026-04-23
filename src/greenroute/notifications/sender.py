# -*- coding: utf-8 -*-
"""
NotificationSender: the single choke point for outbound customer
notifications, for the customer-notifications capability.

fix: move the opted-out check into NotificationSender.send itself so no
send call site can bypass it. Call-site checks are exactly the bug shape
that let three opted-out customers receive reschedule texts -- the
reschedule path built its own send call and skipped the lookup. A caller
cannot bypass consent by forgetting to check it, because send() checks it.
"""
from greenroute.notifications.preferences import is_opted_in


def send(recipient_id, channel, message, preferences_by_customer_channel, provider_send=None):
    """Send `message` to `recipient_id` over `channel`, refusing opted-out
    recipients.

    `provider_send` is a callable(recipient_id, message) -> dict; this
    early version has no registry yet (see
    notifications-provider-abstraction), it just calls whatever provider
    function it is given.
    """
    if not is_opted_in(recipient_id, channel, preferences_by_customer_channel):
        return {"sent": False, "reason": "opted_out"}
    if provider_send is None:
        return {"sent": False, "reason": "no_provider_configured"}
    result = provider_send(recipient_id, message)
    reason = "sent" if result.get("ok") else "provider_error"
    return {"sent": bool(result.get("ok")), "reason": reason}
