# POLICY: PE-21: Electromagnetic Pulse Protection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-21 |
| NIST Control | PE-21: Electromagnetic Pulse Protection |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | electromagnetic pulse, EMP, physical protection, critical infrastructure, shielding, surge protection |

## 1. POLICY STATEMENT
The organization SHALL implement protective measures against electromagnetic pulse (EMP) damage for information systems and system components that require EMP protection. All systems supporting critical infrastructure operations or containing sensitive data MUST be evaluated for EMP vulnerability and protected accordingly.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical Infrastructure Systems | YES | All systems supporting essential operations |
| Data Centers | YES | Primary and backup facilities |
| Network Infrastructure | YES | Core networking and telecommunications equipment |
| End-user Devices | CONDITIONAL | Only if supporting critical operations |
| Cloud Services | CONDITIONAL | Only customer-managed infrastructure components |
| Third-party Facilities | CONDITIONAL | Only if housing critical organization systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Manager | • Implement physical EMP protection measures<br>• Maintain EMP protection equipment<br>• Coordinate with vendors for protection installations |
| CISO | • Define EMP protection requirements<br>• Approve EMP protection strategies<br>• Ensure compliance with regulatory requirements |
| System Owners | • Identify systems requiring EMP protection<br>• Implement system-level protective measures<br>• Report EMP-related incidents |

## 4. RULES

[RULE-01] Organizations MUST identify all information systems and system components that require protection against electromagnetic pulse damage based on criticality assessments.
[VALIDATION] IF system_criticality = "high" OR system_criticality = "critical" AND emp_assessment_completed = FALSE THEN violation

[RULE-02] Protective measures against EMP damage MUST be implemented for all identified critical systems and components within 90 days of identification.
[VALIDATION] IF emp_protection_required = TRUE AND days_since_identification > 90 AND protection_implemented = FALSE THEN violation

[RULE-03] EMP protection measures MUST include at least two of the following: electromagnetic shielding, surge suppressors, ferro-resonant transformers, or proper earth grounding.
[VALIDATION] IF emp_protection_required = TRUE AND protection_methods_count < 2 THEN violation

[RULE-04] All EMP protection equipment MUST be tested annually and after any significant facility modifications or equipment installations.
[VALIDATION] IF emp_equipment_exists = TRUE AND days_since_last_test > 365 THEN violation

[RULE-05] Documentation of EMP protective measures MUST be maintained and updated within 30 days of any changes to protection systems.
[VALIDATION] IF emp_protection_changes = TRUE AND documentation_update_days > 30 THEN violation

[RULE-06] EMP protection systems MUST be monitored continuously where technically feasible, with alerts generated for protection system failures.
[VALIDATION] IF emp_protection_monitoring_capable = TRUE AND monitoring_enabled = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] EMP Risk Assessment - Systematic evaluation of systems requiring EMP protection
- [PROC-02] EMP Protection Implementation - Installation and configuration of protective measures
- [PROC-03] EMP Protection Testing - Annual testing and validation of protection effectiveness
- [PROC-04] EMP Incident Response - Response procedures for EMP events or protection failures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: EMP incidents, facility modifications, new critical system deployments, regulatory changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: New Critical System Deployment]
IF system_criticality = "critical"
AND deployment_date < 30_days_ago
AND emp_assessment_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: EMP Protection Equipment Failure]
IF emp_protection_installed = TRUE
AND protection_system_status = "failed"
AND failure_duration_hours > 24
AND backup_protection_active = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Data Center EMP Protection]
IF facility_type = "data_center"
AND houses_critical_systems = TRUE
AND emp_shielding_installed = TRUE
AND surge_suppressors_installed = TRUE
AND annual_testing_completed = TRUE
THEN compliance = TRUE

[SCENARIO-04: Inadequate Protection Methods]
IF system_requires_emp_protection = TRUE
AND protection_methods_implemented = 1
AND protection_method_type = "surge_suppressor_only"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Third-party Facility Compliance]
IF system_location = "third_party_facility"
AND system_criticality = "high"
AND facility_emp_protection_verified = FALSE
AND verification_overdue_days > 90
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Protective measures employed against EMP damage are defined | [RULE-01], [RULE-03] |
| EMP protection implemented for required systems and components | [RULE-02], [RULE-03] |
| EMP protection measures are maintained and tested | [RULE-04], [RULE-06] |
| Documentation of EMP protective measures is current | [RULE-05] |