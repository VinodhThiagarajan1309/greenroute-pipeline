# Tasks: notifications-baseline

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Send: deliver to a recipient who has opted out; verify with `openspec validate notifications-baseline --strict`
- [x] 1.3 Added requirement in the delta spec: Reminder notifications: fire at T-24h relative to the service window; verify with `openspec validate notifications-baseline --strict`
- [x] 1.4 Added requirement in the delta spec: Opt-out: apply per channel; verify with `openspec validate notifications-baseline --strict`

## 2. Implementation

- [x] 2.1 Add notification_preference table: customer_id, channel, opted_in, updated_at; verify with the tests in this change
- [x] 2.2 Wire confirmation and T-24h reminder sends through the preference lookup; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive notifications-baseline`
