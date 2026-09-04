# -*- coding: utf-8 -*-
# Port the Twilio client from notifications-sms-provider-twilio behind
# the provider registry, so NotificationSender never has to know Twilio
# exists.
from greenroute.notifications.sender import register_provider


def _default_twilio_client():
    """Placeholder for the real Twilio REST client construction
    (credentials, etc.) -- wired up in deployment config, not here.
    """
    raise NotImplementedError("wire up the real Twilio client in deployment config")


def _twilio_provider_send(recipient, message):
    result = send_sms_via_twilio(recipient, message, client=_default_twilio_client())
    return {"ok": result["ok"]}


register_provider("sms", _twilio_provider_send)
