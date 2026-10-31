---
type: readme
language: en
status: draft
updated: 2026-10-30
---

# The Criteria Library (criteria/)

> Adjudication tools distilled from practice discussions, six in all: c1 unified criterion / c2 production–distribution threshold / c3 verification interrogation / c4 verifiability ceiling / c5 continuous attunement / c6 distribution unit. Each entry: definition → judgment → origin → relation to the seed.

## Decision Flow for Using the Criteria

```mermaid
flowchart TD
    X["Assertion / direction"] --> V{"C3 Verification interrogation<br/>Where is the evidence? Who can re-verify?"}
    V -->|"either question vague"| DROP["downgraded to unverified info<br/>must not drive action"]
    V -->|"both questions clear<br/>(level = lowest of chain, L0–L3)"| D{"C2 Production–distribution threshold"}
    D -->|"production ∧ distribution both pass"| GO["may proceed"]
    D -->|"production side only"| HOLD["can be done — but should not"]
    GO --> U{"C1 Unified criterion<br/>Accumulation? Path dependence?<br/>Non-cheap-copyability?"}
    U -->|"all three present"| T["process-nature holds<br/>accumulates as verifiable trajectory (C6)"]
    U -->|"any missing"| F["'product without process'"]
    C4["C4 Verifiability ceiling<br/>(system boundary: beyond it, no promise, no pricing)"] -. constrains .- D
    C5["C5 Continuous attunement<br/>(collaboration form: no mid-state distortion)"] -. constrains .- T
```

## Index

| # | Criterion | One sentence |
|---|---|---|
| C-1 | [Unified criterion](c1-unified-criterion.md) | Process-nature = the capacity to be changed by the process (three independently measurable conditions) |
| C-2 | [Production–distribution threshold](c2-production-distribution-threshold.md) | Production side ∧ distribution side — both gates must pass before proceeding |
| C-3 | [Verification interrogation](c3-verification-interrogation.md) | Where is the evidence + who can re-verify (L0–L3 grading) |
| C-4 | [Verifiability ceiling](c4-verifiability-ceiling.md) | A system's value is capped by its verifiability |
| C-5 | [Continuous attunement](c5-continuous-attunement.md) | The intermediate states are where the real happens |
| C-6 | [Distribution unit](c6-distribution-unit.md) | The verifiable trajectory as the basis of distribution; whatever can be copied should not be the unit |
