# Proposal: Add booking add-ons to the catalog

- **Change id:** `catalog-service-addons`
- **Author:** Jonah Kim
- **Sprint:** 3

## Why

Edging can attach to mowing or to leaf cleanup. Modelling it as a service-type variant
gives a combinatorial catalog; modelling it as a booking attachment does not.

Price freezes at booking time. If we resolved add-on price at billing time instead, a
price change would silently rewrite what already-completed jobs cost.

## What Changes

Adds add-ons as booking-level line items rather than as variants of a service type.

- **ADDED** requirement: an add-on SHALL attach to a booking and SHALL NOT be modelled as a service type variant.
- **ADDED** requirement: add-on price SHALL be resolved and frozen at booking time.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `service-catalog`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/service_catalog/`, `tests/service_catalog/`.
