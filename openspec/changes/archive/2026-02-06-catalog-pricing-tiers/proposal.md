# Proposal: Add zone-based pricing tiers to the catalog

- **Change id:** `catalog-pricing-tiers`
- **Author:** Jonah Kim
- **Sprint:** 2

## Why

Drive time to Round Rock is not drive time to Zilker, and ops has been applying an
informal surcharge by hand. The uniqueness guard exists because the spreadsheet this
replaces had two active mulching prices for four months and invoices depended on row order.

## What Changes

Adds pricing tiers so the same service can carry different prices in core Austin versus
the outer ring, and enforces that exactly one price is active per (service, tier) at a time.

- **ADDED** requirement: each service type SHALL resolve to exactly one active price per zone tier.
- **ADDED** requirement: overlapping active price rows for the same (service, tier) SHALL be rejected at write time.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `service-catalog`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/service_catalog/`, `tests/service_catalog/`.
