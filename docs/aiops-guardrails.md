# AIOps Guardrails

AIOps should reduce operational toil without increasing production blast radius.

Default principles:

- read-only first
- evidence-backed recommendations
- explicit tool permissions
- human approval for production mutation
- sensitive-data redaction
- complete audit trail
- deterministic fallback path
- never make an LLM the only incident-control path

A useful first stage is diagnosis assistance: correlate deploys, alerts, logs, traces, saturation, and known failure modes, then present evidence and a recommended action. Higher-risk remediation should remain approval-gated until it is narrow, deterministic, observable, and reversible.
