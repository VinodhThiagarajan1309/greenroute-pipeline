# Proposal: Make payment capture idempotent on provider_event_id

- **Change id:** `payments-idempotent-capture`
- **Author:** Derek Chen
- **Sprint:** 3

## Why

Closes {{I4}}. The processor retries webhook delivery on any non-2xx response, including
our own timeouts. With no idempotency key, a retried `charge.succeeded` wrote a second row
and the gold ledger double-counted. Four occurrences in production since capture was
enabled.

Enforcing at write time rather than deduplicating in the silver transform is deliberate.
Downstream dedupe would produce correct numbers while leaving the pipeline accepting
duplicate writes, so the next consumer of that table inherits the bug.

## What Changes

Adds an idempotency key on `provider_event_id`, enforced at write time, and repairs the
four duplicate captures already in production.

- **ADDED** requirement: capture SHALL be idempotent on `provider_event_id`; a repeated delivery SHALL NOT create a second ledger entry.
- **ADDED** requirement: payment event ingest SHALL reject duplicates at write time rather than resolving them downstream.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `payments`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/payments/`, `tests/payments/`.

Closes {{I4}}.
