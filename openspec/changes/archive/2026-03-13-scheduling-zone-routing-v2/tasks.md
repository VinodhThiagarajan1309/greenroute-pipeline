# Tasks: scheduling-zone-routing-v2

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Scheduling: own both zone grouping and within-zone stop ordering; verify with `openspec validate scheduling-zone-routing-v2 --strict`
- [x] 1.3 Added requirement in the delta spec: Stop distance used for ordering: be computed as drive time; verify with `openspec validate scheduling-zone-routing-v2 --strict`
- [x] 1.4 Removed requirement in the delta spec: DAB job-parameter config: control zone grouping and stop ordering ownership moved; verify with `openspec validate scheduling-zone-routing-v2 --strict`

## 2. Implementation

- [x] 2.1 feat: move zone grouping and stop ordering into scheduling; verify with the tests in this change
- [x] 2.2 wip: port the drive-time fix from the closed zone-routing PR; verify with the tests in this change
- [x] 2.3 rebase: squash migration and config-knob removal into one commit per review; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive scheduling-zone-routing-v2`
