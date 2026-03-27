# Proposal: Add the technician-compliance capability and TDA license tracking

- **Change id:** `technician-compliance-baseline`
- **Author:** Jonah Kim
- **Sprint:** 6

## Why

`pesticide-service-type` ({{PR:pesticide-service-type}}, sprint 2) put `license_required`
on the catalog row and stopped there, deliberately - design.md from that PR says plainly
that nothing checks the license yet. This is the capability that can answer the question.

It does not answer it at the point that matters. Nothing in scheduling calls this yet -
that's {{PR:pesticide-license-gate}}, not this PR. Landing the data first, gate second,
because the gate needs something to read.

TDA's licensee data resolves to one of active, expired, or suspended per license number.
Matching technicians to license records by license number rather than name - we already
have two technicians named Garcia and matching on name is how you license the wrong one.

## What Changes

Adds `technician-compliance`, which tracks Texas Department of Agriculture (TDA)
applicator license status and expiry per technician.

- **ADDED** requirement: each technician performing a licensed service SHALL have a recorded TDA license_status and expiry_date.
- **ADDED** requirement: license_status SHALL be derived from expiry_date against the current date, not stored as an independently mutable field.
- **ADDED** requirement: a technician SHALL be matched to TDA license records by license number, not by name.

## Capabilities

### New Capabilities

- `technician-compliance`: Texas Department of Agriculture applicator licensing: which technicians may perform which services, and when their licenses expire.

### Modified Capabilities

- None.

## Impact

Affected code: `src/greenroute/compliance/`, `tests/compliance/`.
