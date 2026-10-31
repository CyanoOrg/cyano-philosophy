---
type: evolution-doc
language: en
status: draft
updated: 2026-10-30
source-date: 2026-09-24
---

# The Baseline for Batch Adjudication: Ground Truth from Three Read-Only Verifications

> **The Evolution Archive · Part Two · Entry 5**. 09-24. This entry is **archived as excerpts**: the original was an engineering adjudication working paper (repository-state verification made up most of it); after sanitization, the passages on methodology and philosophical judgment are preserved verbatim, with engineering state compressed into background narration. Editor's note at the end.

---

## Background (the original setting)

Ten pending proposals (accumulated from several preceding discussions) were, before adjudication, checked against the relevant repositories by **three groups of read-only sub-agents** — zero modifications, zero builds, zero pushes throughout; purely refreshing the factual base. The verification exposed drift between "paper records and actual state" in multiple places: version-caliber inconsistencies, misalignment between archived and in-flight work, cross-repo scheduling conflicts, and several artifacts "released with no usage-observation surface."

**The methodological primitive (this entry's archival value)**: verify before adjudicating — trust no paper assertion (including your own); re-assess the factual base read-only; let disagreement be argued only after the facts are refreshed.

## Excerpt 1: The Cross-Cutting Root (§2, verbatim)

> Four product lines share the same structural gap: **what gets released or advanced carries no usage-observation surface.** This is precisely the mirror held up by our own worldview: the reality axiom requires differential change to be verifiable, yet most of our own products "ship and go blind."

(Verification found all four lines hit simultaneously: zero user evidence, zero telemetry, an observation window open but zero records, caliber drift — four manifestations of one disease.)

## Excerpt 2: The Layer-Zero Verdict Proposal (§5, verbatim)

**Verdict line**: [Layer-Zero verdict] **conditional** — the reality axiom (differential change verifiable) says "no" to "releases without an observation surface": **a released artifact must carry a minimal usage-observation surface, or it is not released.**

- Proposed primitive: **minimum usage observability** — at release time, the artifact already has a minimal observable implementation of "whether use happened, where it happened, what change-signal it produced" (local statistics suffice; remote telemetry not required — aligned with the privacy and sovereignty axioms).
- Applicability ruling: release is not a terminal action but the start of verifiable responsibility — an artifact without an observation surface = differential change unverifiable = a violation of the reality axiom.

## Excerpt 3: The Shape of the Ruling (§6, condensed)

All ten proposals were settled as "verify-then-revise recommendations" — three were **re-ruled** on verified facts (the original proposals rested on stale assumptions), one was merged for a scheduling conflict, and two new items (a caliber correction, a release precondition) were established on the spot. A ruling takes effect on refreshed facts, not on the eloquence of the proposal.

---

## Editor's Note

**What this discussion changed at the time**: verification interrogation (where is the evidence / who can re-verify) ran for the first time as an **organization-level process** — all ten rulings passed read-only verification first; three proposals were re-ruled on the spot by verified facts. **The disagreement was not in opinions but in evidence levels**: things the paper said "passed" turned out, on verification, to be "approved ≠ executed"; things the paper said "soaking" showed zero records in the observation window. After that day, "verify before adjudicating" became the default discipline.

**Links to the canon**: → [c3 verification interrogation](../../criteria/en/c3-verification-interrogation.md) (this entry is its practice site — the organizational application of "a chain's level is its lowest link"); → the A4 reality axiom ("released but usage invisible" = differential change unverifiable, at organizational scale).

**Lines of evolution**: the four axioms (entry 3) were the propositions; the unified criterion (entry 4), the mechanism; this entry is the **first large-scale practice** — philosophy moving from "what we believe" to "how we adjudicate." §5's "minimum usage observability" primitive was adopted the same day as an organization-level ruling — the first governance rule directly produced by the reality axiom.

**The posture of "read-only verification"**: note the design — three parallel groups, read-only throughout, zero modifications, zero builds, zero pushes. The verifier's restraint is itself the discipline: **the verifier's task is to put facts on the table, not to decide for the adjudicator.** This posture later became the default form of all review work.
