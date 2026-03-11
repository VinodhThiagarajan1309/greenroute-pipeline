# Tasks: scheduling-reschedule-v2

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Reschedule: invalidate every derived route assignment for the booking's; verify with `openspec validate scheduling-reschedule-v2 --strict`
- [x] 1.3 Added requirement in the delta spec: Reschedule: preserve the booking's identity and history; verify with `openspec validate scheduling-reschedule-v2 --strict`

## 2. Implementation

- [x] 2.1 wip: reschedule as cancel+rebook instead of an in-place booking update; verify with the tests in this change
- [x] 2.2 actually, cancel+rebook loses the audit trail on why the job moved. backing; verify with the tests in this change
- [x] 2.3 fix: reschedule now explicitly invalidates route assignment for the original; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive scheduling-reschedule-v2`
