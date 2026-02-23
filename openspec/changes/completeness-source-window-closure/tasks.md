# Tasks: completeness-source-window-closure

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Gold publish: block until every contributing source watermark has closed; verify with `openspec validate completeness-source-window-closure --strict`
- [x] 1.3 Added requirement in the delta spec: Blocked publish: emit a metric identifying the source that blocked; verify with `openspec validate completeness-source-window-closure --strict`

## 2. Implementation

- [x] 2.1 Add explicit window-closure gate before gold publish; verify with the tests in this change
- [x] 2.2 Emit a metric when the gate blocks, so we can see how often it actually fires; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive completeness-source-window-closure`
