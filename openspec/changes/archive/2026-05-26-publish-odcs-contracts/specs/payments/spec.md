# payments Delta

Change `publish-odcs-contracts`: Publish ODCS contracts for the gold tables

## ADDED Requirements

### Requirement: Gold_payment_ledger: publish and maintain an ODCS contract linked

`gold_payment_ledger` SHALL publish and maintain an ODCS contract linked to this capability via `customProperties`.

#### Scenario: Publish and maintain an ODCS contract linked to this

- **WHEN** `gold_payment_ledger` is exercised in a published window
- **THEN** `gold_payment_ledger` SHALL publish and maintain an ODCS contract linked to this capability via `customProperties`
- **AND** the outcome is visible in the job's emitted metrics
