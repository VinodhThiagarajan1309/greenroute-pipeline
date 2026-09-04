# Proposal: Add the pesticide-application service type

- **Change id:** `pesticide-service-type`
- **Author:** Jonah Kim
- **Sprint:** 2

## Why

Texas Department of Agriculture rules require a licensed applicator for commercial
pesticide application. Ops has been handling this by only assigning certain technicians
by hand. That works until it doesn't.

Deliberately putting the constraint on the catalog row as a flag rather than hardcoding
"if service == 'pesticide'". Fertilizer will need the same treatment, and I'd rather not
have that as a second special case bolted onto the first.

## What Changes

Adds pesticide application as a catalog service type, carrying a `license_required` flag.

- **ADDED** requirement: a service type SHALL declare whether it requires a licensed applicator.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `service-catalog`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/service_catalog/`, `tests/service_catalog/`.
