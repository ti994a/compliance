```markdown
# POLICY: SC-6: Resource Availability

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-6 |
| NIST Control | SC-6: Resource Availability |
| Version | 1.0 |
| Owner | Infrastructure Security Manager |
| Keywords | resource allocation, availability protection, priority processes, quotas, system resources |

## 1. POLICY STATEMENT
The organization SHALL protect system availability by implementing resource allocation mechanisms that prioritize critical processes and prevent resource exhaustion. Resource allocation policies MUST define priority levels and establish quotas to prevent lower-priority processes from interfering with higher-priority operations.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing business-critical data |
| Development Systems | YES | Systems with shared resources or production dependencies |
| Cloud Infrastructure | YES | All IaaS, PaaS, and hybrid cloud environments |
| Network Infrastructure | YES | Routers, switches, and network appliances |
| End-user Devices | CONDITIONAL | Only devices providing critical services |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Infrastructure Security Manager | • Define resource allocation policies<br>• Approve priority classifications<br>• Monitor compliance with allocation rules |
| System Administrators | • Implement resource quotas and limits<br>• Configure priority-based scheduling<br>• Monitor resource utilization |
| Application Owners | • Define application resource requirements<br>• Request appropriate priority classifications<br>• Monitor application performance |

## 4. RULES

[RULE-01] All systems MUST implement resource allocation mechanisms that prioritize processes based on defined business criticality levels.
[VALIDATION] IF system_type = "production" AND resource_allocation_configured = FALSE THEN critical_violation

[RULE-02] Resource quotas MUST be established for CPU, memory, storage, and network bandwidth to prevent resource exhaustion by individual processes or users.
[VALIDATION] IF quota_type IN ["cpu", "memory", "storage", "bandwidth"] AND quota_configured = FALSE THEN violation

[RULE-03] Priority classifications MUST be documented and approved by the Infrastructure Security Manager before implementation.
[VALIDATION] IF priority_level = "high" AND approval_status != "approved" THEN violation

[RULE-04] Lower-priority processes MUST NOT be able to consume more than 70% of available system resources during peak usage periods.
[VALIDATION] IF process_priority = "low" AND resource_consumption > 70% AND peak_hours = TRUE THEN violation

[RULE-05] Critical business processes MUST be guaranteed a minimum of 80% of required resources even during system stress conditions.
[VALIDATION] IF process_criticality = "critical" AND available_resources < 80% THEN critical_violation

[RULE-06] Resource allocation configurations MUST be reviewed and validated quarterly to ensure alignment with current business priorities.
[VALIDATION] IF last_review_date > 90_days AND review_status = "pending" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Resource Priority Classification - Process for assigning and approving business criticality levels
- [PROC-02] Quota Management - Procedures for establishing and maintaining resource quotas
- [PROC-03] Performance Monitoring - Continuous monitoring of resource utilization and allocation effectiveness
- [PROC-04] Incident Response - Response procedures for resource exhaustion events

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major infrastructure changes, performance incidents, business priority changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Batch Job Resource Consumption]
IF process_type = "batch_job"
AND resource_consumption > 70%
AND business_hours = TRUE
AND priority_level = "low"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Critical Service Resource Guarantee]
IF service_criticality = "critical"
AND allocated_resources < 80%
AND system_load > "normal"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Unapproved High Priority Process]
IF priority_classification = "high"
AND approval_status = "pending"
AND deployment_status = "active"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Resource Quota Exceeded]
IF user_consumption > assigned_quota
AND quota_type IN ["cpu", "memory", "storage"]
AND enforcement_enabled = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant Resource Allocation]
IF resource_quotas_configured = TRUE
AND priority_scheduling_enabled = TRUE
AND critical_services_guaranteed = TRUE
AND approval_status = "current"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Resources allocated by priority | [RULE-01], [RULE-03] |
| Availability protection mechanisms | [RULE-02], [RULE-05] |
| Prevention of interference | [RULE-04] |
| Resource allocation documentation | [RULE-03], [RULE-06] |
```