# Tasks: completeness-watermarks

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Gold partition: publish until every contributing source watermark has closed; verify with `openspec validate completeness-watermarks --strict`
- [x] 1.3 Added requirement in the delta spec: Each source: declare a maximum expected lateness; verify with `openspec validate completeness-watermarks --strict`

## 2. Implementation

- [x] 2.1 Add watermark table tracking max observed lateness per source; verify with the tests in this change
- [x] 2.2 Set the cancellation watermark to 48h based on the measured p99 of 11h and max; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive completeness-watermarks`
