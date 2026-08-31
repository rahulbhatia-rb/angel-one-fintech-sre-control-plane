# Angel One Fintech SRE Control Plane

Independent proof-of-work inspired by the Angel One SRE 2/3 role.

This project models a production-readiness contract for a large-scale fintech platform where reliability, resilience, security, developer velocity, incident leadership, cost, and operational intelligence all need to be treated as one system.

It does **not** represent Angel One's private architecture.

## Core idea

```text
Service / Platform Change
        |
        v
IaC + CI/CD + GitOps
        |
        +--> EKS / AWS controls
        +--> Security / IAM
        +--> Observability / SLOs
        +--> Capacity / Cost
        +--> DR / Resilience
        +--> AIOps guardrails
        |
        v
Reliability Contract
        |
        +--> static evidence
        +--> runtime evidence
        +--> ownership evidence
        |
        v
Progressive rollout -> production validation -> rollback / incident ownership
```

## Why this maps to Angel One

A fintech SRE role at this scale is not just about keeping clusters alive. The platform has to protect customer-facing financial journeys during deploys, dependency failures, traffic spikes, cloud incidents, and operational mistakes.

The useful abstraction is therefore a **reliability contract**: a workload is not production-ready because Kubernetes accepted it. It is ready only when resilience, observability, security, rollback, capacity, cost, ownership, and recovery evidence are all present.

## Contract areas

### Kubernetes / EKS
Workload identity, least privilege, requests/limits, HPA, PDB, multi-AZ placement, topology spread, private networking, ingress controls, approved registries, and lifecycle ownership.

### Terraform / IaC
Reusable modules, remote state + locking, version pinning, plan-before-apply, policy validation, drift detection, environment isolation, and recovery/import procedure.

### CI/CD + GitOps
Tests, security scans, immutable artifacts, GitOps deployment, progressive rollout, production validation, automated rollback, and deployment markers.

### SLO / Observability
Service SLIs, availability and latency SLOs, error budgets, burn-rate alerts, logs, metrics, traces, customer-impact signals, runbooks, and ownership.

### DR / Resilience
RTO, RPO, backups, restore testing, multi-AZ, dependency failure modes, failover testing, game days, and business-continuity ownership.

### Incident Engineering
Severity model, incident commander, timeline, mitigation owner, customer impact, RCA owner, permanent corrective action, regression guard, and follow-up deadline.

### Security
IAM least privilege, RBAC, secrets management, encryption, audit evidence, vulnerability scanning, network segmentation, and controlled break-glass.

### Capacity / Performance / Cost
Capacity model, headroom threshold, saturation signals, scaling limits, downstream dependency capacity, cost ownership, anomaly alerts, rightsizing review, and purchase-model decisions.

### AIOps / GenAI
Read-only by default, explicit tool boundaries, no default production mutation, human approval for high-risk actions, audit trail, sensitive-data redaction, evidence-backed recommendations, and deterministic fallback.

### Engineering Leadership
Service owner, architecture review, operational-readiness review, exception owner/expiry, knowledge-transfer artifacts, and cross-team dependency ownership.

## Where contract values come from

The JSON examples are only a PoC interface. In production, evidence should be collected automatically from Terraform plan/state, Kubernetes and Helm, ArgoCD/Jenkins/GitHub Actions, AWS APIs and CloudWatch, Prometheus/Grafana/tracing, service catalogs, incident systems, and FinOps data.

Developers declare intent; the platform collects evidence.

## Run

```bash
python -m unittest -v tests.test_gate
python src/cli.py examples/production.json
python src/cli.py examples/unsafe.json
```

## 30 / 60 / 90

### 0-30 days
Map critical user journeys and Tier-0/Tier-1 services, understand EKS/AWS topology and incident patterns, baseline SLOs/MTTR/error-budget burn/change-failure rate, identify toil, and map DR gaps.

### 31-60 days
Standardize reliability contracts and golden paths, tighten GitOps and progressive delivery, improve burn-rate/customer-impact alerting, automate evidence collection, run restore/failover exercises, and prioritize capacity/cost opportunities.

### 61-90 days
Reduce repeat incidents through systemic corrective actions, automate frequent diagnostics/remediation, improve multi-team reliability governance, introduce controlled AIOps assistance, and establish regular resilience/capacity reviews.

## Metrics

SLO attainment, error-budget burn, change failure rate, MTTR/MTTD, repeat incidents, recovery-test success, restore time vs RTO, capacity headroom, deployment rollback rate, operational toil, cloud cost, and expired reliability exceptions.

## Disclaimer

Independent public-JD prototype; no claim is made about Angel One's internal architecture, controls, or systems.
