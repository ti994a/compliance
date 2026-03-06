```markdown
# POLICY: SC-6: Resource Availability

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-6 |
| NIST Control | SC-6: Resource Availability |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | resource allocation, availability, priority, quotas, system resources, performance |

## 1. POLICY STATEMENT
The organization SHALL protect system availability by implementing resource allocation controls that prioritize critical processes and prevent resource exhaustion. All systems MUST enforce resource quotas and priority-based allocation to ensure higher-priority processes are not impacted by lower-priority activities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All customer-facing and business-critical systems |
| Development Systems | YES | When hosting shared development resources |
| Cloud Infrastructure | YES | Including auto-scaling and resource management |
| Network Infrastructure | YES | Bandwidth and connection prioritization |
| End-user Devices | CONDITIONAL | Only for systems processing sensitive data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure resource quotas and limits<br>• Monitor resource utilization<br>• Implement priority-based scheduling |
| Security Team | • Define resource protection requirements<br>• Review resource allocation policies<br>• Monitor for resource-based attacks |
| Operations Team | • Monitor system performance<br>• Respond to resource exhaustion incidents<br>• Maintain resource allocation documentation |

## 4. RULES

[RULE-01] All production systems MUST implement resource quotas that prevent any single user or process from consuming more than 80% of available CPU, memory, or storage resources.
[VALIDATION] IF resource_utilization_by_single_entity > 80% AND quota_enforcement = FALSE THEN violation

[RULE-02] Critical business processes MUST be assigned higher priority levels than non-critical processes in system scheduling and resource allocation.
[VALIDATION] IF critical_process_priority <= non_critical_process_priority THEN violation

[RULE-03] Resource allocation policies MUST be documented and include specific quotas for CPU, memory, storage, and network bandwidth for each service tier.
[VALIDATION] IF resource_policy_documented = FALSE OR quota_specifications_missing = TRUE THEN violation

[RULE-04] Systems MUST implement automated monitoring that alerts when resource utilization exceeds 85% for any critical resource type.
[VALIDATION] IF resource_utilization > 85% AND alert_generated = FALSE THEN violation

[RULE-05] Resource allocation controls MUST be tested quarterly to verify proper priority enforcement and quota limitations.
[VALIDATION] IF last_resource_test_date > 90_days_ago THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Resource Quota Configuration - Standard process for setting and maintaining resource limits
- [PROC-02] Priority Classification - Method for classifying and assigning process priorities
- [PROC-03] Resource Monitoring - Continuous monitoring and alerting procedures
- [PROC-04] Incident Response - Response procedures for resource exhaustion events

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, system architecture changes, performance degradation events

## 7. SCENARIO PATTERNS

[SCENARIO-01: Database Resource Exhaustion]
IF system_type = "database_server"
AND single_query_cpu_usage > 80%
AND resource_quotas_enabled = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Proper Priority Implementation]
IF critical_process_priority = "HIGH"
AND background_process_priority = "LOW"
AND priority_enforcement = TRUE
THEN compliance = TRUE

[SCENARIO-03: Cloud Auto-scaling Without Limits]
IF deployment_type = "cloud"
AND auto_scaling_enabled = TRUE
AND resource_limits_configured = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Monitoring Gap]
IF resource_utilization = 90%
AND monitoring_enabled = TRUE
AND alert_generated = FALSE
AND alert_threshold > 85%
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Quarterly Testing Overdue]
IF last_resource_allocation_test > 95_days_ago
AND system_classification = "production"
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Resources allocated by priority | [RULE-02] |
| Resource availability protection | [RULE-01], [RULE-04] |
| Quota implementation | [RULE-01], [RULE-03] |
| Priority-based allocation | [RULE-02] |
| Resource monitoring | [RULE-04] |
| Testing and validation | [RULE-05] |
```