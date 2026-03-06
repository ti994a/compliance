# POLICY: CP-2.7: Coordinate with External Service Providers

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CP-2.7 |
| NIST Control | CP-2.7: Coordinate with External Service Providers |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | contingency planning, external service providers, coordination, service level agreements, business continuity |

## 1. POLICY STATEMENT
The organization SHALL coordinate its contingency plans with external service providers to ensure comprehensive continuity coverage for all mission-critical functions. All external dependencies MUST be identified, documented, and incorporated into the organization's overall contingency planning framework.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All external service providers | YES | Supporting mission-critical functions |
| Cloud service providers | YES | IaaS, PaaS, SaaS platforms |
| Managed service providers | YES | IT operations, security services |
| Third-party software vendors | CONDITIONAL | Only if providing critical business functions |
| Suppliers/Vendors | CONDITIONAL | Only if supporting IT infrastructure |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Business Continuity Manager | • Coordinate contingency planning with external providers<br>• Maintain external provider contingency documentation<br>• Conduct regular coordination reviews |
| Vendor Management Office | • Ensure SLAs include contingency requirements<br>• Monitor provider contingency capabilities<br>• Facilitate contingency plan coordination |
| IT Operations Manager | • Identify technical dependencies on external providers<br>• Test integrated contingency procedures<br>• Maintain provider contact information |

## 4. RULES
[RULE-01] All external service providers supporting mission-critical functions MUST provide their contingency plans for coordination review within 30 days of contract execution.
[VALIDATION] IF provider_supports_critical_function = TRUE AND contingency_plan_received = FALSE AND days_since_contract > 30 THEN violation

[RULE-02] Service Level Agreements (SLAs) with external providers MUST include specific contingency requirements, recovery time objectives (RTOs), and recovery point objectives (RPOs) aligned with organizational requirements.
[VALIDATION] IF sla_exists = TRUE AND (contingency_requirements_defined = FALSE OR rto_defined = FALSE OR rpo_defined = FALSE) THEN violation

[RULE-03] Contingency plan coordination reviews with external providers MUST be conducted at least annually and within 30 days of any significant changes to provider services or organizational requirements.
[VALIDATION] IF last_coordination_review > 365_days OR (significant_change_occurred = TRUE AND days_since_change > 30 AND coordination_review_completed = FALSE) THEN violation

[RULE-04] External provider contingency capabilities MUST be tested as part of the organization's contingency plan testing at least annually.
[VALIDATION] IF provider_supports_critical_function = TRUE AND last_joint_test > 365_days THEN violation

[RULE-05] Organizations MUST maintain current emergency contact information for all external service providers supporting mission-critical functions.
[VALIDATION] IF provider_supports_critical_function = TRUE AND (emergency_contacts_missing = TRUE OR contact_verification_age > 180_days) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External Provider Contingency Assessment - Evaluate and document provider contingency capabilities
- [PROC-02] Contingency Plan Coordination - Integrate provider plans with organizational contingency planning
- [PROC-03] Joint Contingency Testing - Conduct coordinated testing with external providers
- [PROC-04] Provider Contingency Monitoring - Ongoing monitoring of provider contingency readiness

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New critical external providers, significant service changes, contingency plan updates, provider security incidents

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Critical Cloud Provider]
IF new_provider = TRUE
AND supports_critical_function = TRUE
AND contract_signed = TRUE
AND contingency_plan_coordination_completed = FALSE
AND days_since_contract > 30
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Provider Contingency Plan Outdated]
IF provider_contingency_plan_received = TRUE
AND provider_plan_last_updated > 365_days
AND coordination_review_requested = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Missing SLA Contingency Requirements]
IF sla_exists = TRUE
AND provider_supports_critical_function = TRUE
AND contingency_requirements_in_sla = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Successful Joint Testing]
IF provider_supports_critical_function = TRUE
AND joint_contingency_test_completed = TRUE
AND test_date < 365_days
AND test_results_documented = TRUE
THEN compliance = TRUE

[SCENARIO-05: Provider Emergency Contact Verification]
IF provider_supports_critical_function = TRUE
AND emergency_contacts_documented = TRUE
AND last_contact_verification < 180_days
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Contingency plan coordination with external service providers | RULE-01, RULE-03 |
| Contingency requirements satisfaction verification | RULE-02, RULE-04 |
| External provider contingency capability assessment | RULE-01, RULE-04 |
| Ongoing coordination maintenance | RULE-03, RULE-05 |