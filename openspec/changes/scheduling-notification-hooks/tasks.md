# Tasks: scheduling-notification-hooks

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Modified requirement in the delta spec: Send: deliver to a recipient who has opted out; verify with `openspec validate scheduling-notification-hooks --strict`
- [x] 1.3 Added requirement in the delta spec: Reschedule path: send notifications through NotificationSender; verify with `openspec validate scheduling-notification-hooks --strict`

## 2. Implementation

- [x] 2.1 fix: reschedule now checks notification_preference before sending the; verify with the tests in this change
- [x] 2.2 fix: move the opted-out check into NotificationSender.send itself so no send; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive scheduling-notification-hooks`
