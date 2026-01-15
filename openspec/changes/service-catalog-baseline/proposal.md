# Proposal: Add the service-catalog capability as the authority on service types and pricing

- **Change id:** `service-catalog-baseline`
- **Author:** Derek Chen
- **Sprint:** 1

## Why

Service types are currently implied by strings in the booking payload (`"mow"`, `"mowing"`,
`"MOW_STD"` all appear in the last 90 days of data). Pricing lives in an ops spreadsheet.
Neither is queryable, and neither can be pointed at when two systems disagree.

## What Changes

Introduces `service-catalog`: the capability that decides what GreenRoute sells, what it
costs, and what constraints attach to selling it.

- **ADDED** requirement: the catalog SHALL define exactly one active row per billable service type.
- **ADDED** requirement: a booking referencing an unknown service type SHALL be quarantined, not defaulted.

## Capabilities

### New Capabilities

- `service-catalog`: What GreenRoute sells: service types, add-ons, pricing tiers, and the constraints that attach to selling a given service.

### Modified Capabilities

- None.

## Impact

Affected code: `src/greenroute/service_catalog/`, `tests/service_catalog/`.
