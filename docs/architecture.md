# Architecture

Evidence collectors feed a reliability-policy engine.

## Static evidence

- Terraform plans and state
- Kubernetes and Helm configuration
- CI/CD and GitOps definitions
- service ownership metadata

## Runtime evidence

- EKS and AWS APIs
- Prometheus and Grafana
- logs and traces
- deployment health
- capacity and saturation
- recovery-test results

The gate should block unsafe production promotion or require an explicit, owned, expiring exception. The PoC keeps evidence as JSON so the policy behavior is easy to inspect; a production implementation would derive it automatically from the systems above.
