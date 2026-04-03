# Tasks: orchestration-retry-policy

## 1. Specification

- [x] 1.1 Write proposal.md and agree the direction in review
- [x] 1.2 Added requirement in the delta spec: Job failure: be classified retryable or fatal at the point; verify with `openspec validate orchestration-retry-policy --strict`
- [x] 1.3 Added requirement in the delta spec: Failed data-completeness or data-correctness gate: be classified fatal; verify with `openspec validate orchestration-retry-policy --strict`
- [x] 1.4 Added requirement in the delta spec: Retryable failure: retry at most 3 times with backoff; verify with `openspec validate orchestration-retry-policy --strict`

## 2. Implementation

- [x] 2.1 Add job-level retry policy: classify failures retryable or fatal; verify with the tests in this change
- [x] 2.2 A failed completeness or correctness gate is classified fatal; verify with the tests in this change
- [x] 2.3 Transient infra failures retry 3x with backoff; verify with the tests in this change

## 3. Verification

- [x] 3.1 Tests cover every scenario in the delta; verify with `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict` and `pytest`
- [x] 3.3 Review addressed and change archived with `openspec archive orchestration-retry-policy`
