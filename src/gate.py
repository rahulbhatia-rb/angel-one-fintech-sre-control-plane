from typing import Any, Dict

REQUIRED = {
    "eks": ["workload_identity", "least_privilege", "requests_limits", "hpa", "pdb", "multi_az", "topology_spread", "private_networking", "ingress_control", "approved_registry", "lifecycle_owner"],
    "iac": ["reusable_modules", "remote_state", "locking", "version_pinning", "plan_required", "policy_validation", "drift_detection", "env_isolation", "recovery_procedure"],
    "delivery": ["tests", "security_scan", "immutable_artifact", "gitops", "progressive_rollout", "production_validation", "automated_rollback", "deployment_marker"],
    "observability": ["service_sli", "availability_slo", "latency_slo", "error_budget", "burn_rate_alerts", "logs", "metrics", "traces", "customer_impact_signal", "runbook", "owner"],
    "resilience": ["rto", "rpo", "backup", "restore_test", "multi_az", "dependency_failure_mode", "failover_test", "game_day", "bc_owner"],
    "incident": ["severity_model", "incident_commander", "timeline", "mitigation_owner", "customer_impact", "rca_owner", "permanent_corrective_action", "regression_guard", "followup_deadline"],
    "security": ["iam_least_privilege", "rbac", "secrets_manager", "encryption_at_rest", "encryption_in_transit", "audit_evidence", "vulnerability_scan", "network_segmentation", "break_glass"],
    "capacity_cost": ["capacity_model", "headroom_threshold", "saturation_signal", "scaling_limit", "dependency_capacity", "cost_owner", "budget_alert", "rightsizing_review", "purchase_model_decision"],
    "aiops": ["read_only_default", "tool_boundaries", "no_default_prod_mutation", "human_approval", "audit_trail", "sensitive_data_redaction", "evidence_attached", "deterministic_fallback"],
    "leadership": ["service_owner", "architecture_review", "operational_readiness_review", "exception_owner", "exception_expiry", "knowledge_transfer", "cross_team_dependency_owner"],
}


def evaluate(spec: Dict[str, Any]) -> Dict[str, Any]:
    findings = []
    for section, fields in REQUIRED.items():
        values = spec.get(section, {})
        for field in fields:
            if not values.get(field):
                findings.append(f"{section}.{field} is required")
    return {"allowed": not findings, "findings": findings}
