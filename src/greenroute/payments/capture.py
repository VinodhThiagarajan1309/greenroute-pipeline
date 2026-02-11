# -*- coding: utf-8 -*-
"""payments: idempotent capture writes, keyed on provider_event_id.

The processor retries webhook delivery on any non-2xx response, including
our own timeouts. Capture must be safe to receive the same
provider_event_id more than once.
"""


def capture_already_applied(provider_event_id, existing_capture_event_ids):
    """True if this provider_event_id has already been captured.

    Checked on the retry path before anything else: if the processor
    redelivers a webhook we've already captured, this call makes the retry
    a no-op.
    """
    return provider_event_id in existing_capture_event_ids
