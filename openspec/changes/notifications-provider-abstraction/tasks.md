# Tasks: notifications-provider-abstraction

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Notification sends: go through the NotificationSender interface; verify with `openspec validate notifications-provider-abstraction --strict`
- [x] 1.3 Added requirement in the delta spec: Provider: register against one or more channels; verify with `openspec validate notifications-provider-abstraction --strict`

## 2. Implementation

- [x] 2.1 Define NotificationSender interface: send(recipient, channel, template; verify with the tests in this change
- [x] 2.2 Add provider registry keyed by channel; verify with the tests in this change
- [x] 2.3 Port the Twilio client from notifications-sms-provider-twilio behind; verify with the tests in this change
- [x] 2.4 Move confirmation, reminder; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive notifications-provider-abstraction`
