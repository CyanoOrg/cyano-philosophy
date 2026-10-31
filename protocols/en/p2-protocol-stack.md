---
type: protocol
language: en
status: draft
updated: 2026-10-31
---

# P-2 The Protocol Stack: Layered Iteration

## Definition

The protocol stack is the **iterative architecture** through which the agora protocol lands — not a system built in one stroke, but a four-step staircase: each layer resolves one class of dispute, maturity increasing from bottom to top (verification most mature, distribution most theoretical). **The theory–execution scissors gap is drawn across these steps.**

Relation to the [P-1 Agora Protocol](p1-agora.md): P-1 defines the protocol's properties and governance form (what it is); this document defines its growth path (how it grows).

## Layered Iteration (maturity decreasing top to bottom)

### ① Verification Layer — undisputed facts (maturity: already exists in practice)

- **Mechanism**: replay settles it, machines rule; absorbs most "factual disputes."
- Built-in verification is one of the protocol's necessary properties ([p1 · Necessary properties], ④) — this layer is not an add-on but the protocol's foundation.

### ② Mutual-Recognition Layer — standards moved up front (maturity: adjacent action, may begin)

- **Mechanism**: move "standards disputes" up front into contracts — a receipt verified in domain A can be verified in domain B; **evidence is mutually recognized, decision rights are not touched**.
- This is the nearest actionable point: do not presuppose the agora ontology; first make receipts cross-verifiable.

### ③ Adjudication Layer — disputes converge (maturity: prototype in internal practice)

**Three dispute types** (the adjudication layer handles only the third): factual disputes → mostly absorbed by the verification layer; standards disputes → mostly pre-empted by mutual recognition; **liability disputes (counterfactuals / intent / externalities) → the core of the adjudication layer**.

**Tiered courts** (each tier an order of magnitude cheaper; the tier above is the appellate court of the tier below; the terminal tier auto-suggested by the dispute's stake — a damping design):

| Tier | Form | Cost |
|---|---|---|
| L0 automatic | rules built into the protocol | zero human labor |
| L1 reconciliation | two parties + trajectory, three-way reconciliation | most disputes end here |
| L2 arbitration network | reputation-drawn lots, agents first, humans retain final veto | low |
| L3 legal system | real-world courts (persons / criminal / above jurisdictional thresholds) | real-world cost |

**The minimal-core trio** (more is over-design): ① **trajectory replay** — evidence-gathering cost ≈ 0, the basis of adjudication economics; ② **prefabricated stakes** — staked or insured, self-executing on breach; ③ **a citation syntax for precedents** — common-law style, precedents forkable and metabolizing with versions.

**Design principles**: the goal = minimal court-entry rate (the idler the better); adjudication built into the trajectory (gevulot's dual role: pricing in peacetime, evidence in dispute); precedents are alive; the right of exit = the ultimate check.

**Red line**: on-chain executes, never adjudicates — rulings enter the chain as data for execution; the chain itself has no jurisdiction (structural protection against casino-ization).

### ④ Distribution Layer — value reflow (maturity: theory, long-term clause)

- The distribution unit = the verifiable trajectory (not the product snapshot); visibility = the pricing function; the reflow contract + the commons pool (pricing maintenance-grade entropy reduction) — details in P-1.
- Known precondition gaps: loop velocity and the metering of cognitive capital are undefined; the commons pool is not yet engineered.

## The Five-Step Approach Path (a sequential view; isomorphic to the layers — layer and sequence confirm each other)

1. **Design receipts for outside verifiers** (the verification layer's self-proof, extended)
2. **Cross-domain citation** — a domain-A receipt verified in domain B (mutual recognition's first concrete act)
3. **Extend the adjudication domain** — contractualize and pilot dispute rulings
4. **A lightweight multi-person trial field** — the agora prototype's minimal multi-party form
5. **The unforgeable layer** — run history as externally verifiable asset (foundation and storefront are the same thing)

**On-paper discipline**: the unlock condition for the agora protocol proper = the first outside verifier of the unforgeable layer — until then, cross-domain receipt citation and verification-layer building proceed unrestricted (they are the foundation, not the agora).

## Origin

2026-09 cognitive co-creation network discussion series (iteration path and adjudication-layer design); principle-layer rulings on 2026-09-24/26.

## Relation to the Seed

The differential branch landing as a staircase: verification → mutual recognition → adjudication → distribution — each layer is "not cheaply fakeable" advanced one step in collaborative depth: the verification layer makes facts hard to fake, the adjudication layer makes liability hard to escape, the distribution layer makes contribution hard to misappropriate. The sovereignty branch's guarantees: the right of exit and the "on-chain never adjudicates" red line.
