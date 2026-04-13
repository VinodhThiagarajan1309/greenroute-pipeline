# Proposal: License gate covers every service the catalog flags license_required, not only pesticide

- **Change id:** `license-gate-all-licensed-services`
- **Author:** Jonah Kim
- **Sprint:** 7

## Why

Ops asked whether the gate covers "the weed guys". It did not. Their service rows were created
in sprint 2 with `license_required=false`, before anyone had written a gate that would read it.
Same failure shape as {{I11}}, one service type over: the data was wrong instead of unread.

The catalog requirement is the durable half. Once every service type declares the flag
explicitly and the gate reads only the flag, adding a licensed service is a catalog row, not a
scheduling change.

## What Changes

The requirement has said "licensed-service" since Apr 4, but the scenario, the tests and the
catalog only ever meant pesticide. TDA licenses herbicide and fertilizer application under the
same rule. This change makes the requirement say so, and flags those two service types
`license_required` in the catalog, which is the only thing the gate reads.

- **MODIFIED** requirement: scheduling SHALL reject confirmation of a licensed-service booking when the assigned technician's license_status is not active, for every service type the catalog flags license_required, unless the status is pending_renewal filed on or before expiry and within 30 days of it.
- **ADDED** requirement: each service type SHALL declare license_required explicitly, and the scheduling gate SHALL read that flag rather than a list of service names.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `scheduling`: requirements change as listed above.
- `service-catalog`: requirements change as listed above.

## Impact

Affected code: `src/greenroute/scheduling/`, `src/greenroute/service_catalog/`, `tests/scheduling/`, `tests/service_catalog/`.
