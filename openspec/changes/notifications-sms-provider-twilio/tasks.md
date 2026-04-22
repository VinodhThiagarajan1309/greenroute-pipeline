# Tasks: notifications-sms-provider-twilio

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: SMS delivery: use the Twilio Messages API; verify with `openspec validate notifications-sms-provider-twilio --strict`

## 2. Implementation

- [x] 2.1 Wire confirmation, reminder; verify with the tests in this change
- [x] 2.2 Add Twilio client wrapper: send SMS via the Messages API; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [ ] 3.3 Review addressed and change archived with `openspec archive notifications-sms-provider-twilio`
